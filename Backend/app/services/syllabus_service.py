from datetime import datetime, timedelta
from math import ceil
from bson import ObjectId
from ..database import db
from ..models.syllabus_model import syllabus_plan_document


def _date_diff_in_weeks(start: datetime, end: datetime) -> int:
    delta = end - start
    return max(1, delta.days // 7)


async def generate_syllabus_plan(batchId: str, courseId: str, startDate: str, endDate: str, examDate: str = None, classesPerWeek: int = 3, generatedBy: str = 'AI'):
    # parse dates
    s = datetime.fromisoformat(startDate)
    e = datetime.fromisoformat(endDate)
    total_weeks = max(1, (e - s).days // 7)
    total_classes = total_weeks * classesPerWeek

    # fetch course chapters if available
    try:
        course = await db.courses.find_one({'_id': ObjectId(courseId)})
        chapters = course.get('chapters', []) if course else []
    except Exception:
        chapters = []

    if not chapters:
        # fallback dummy chapters
        chapters = [{'title': f'Chapter {i+1}'} for i in range(6)]

    # allocate classes across chapters proportionally
    num_chapters = max(1, len(chapters))
    base_per_chapter = total_classes // num_chapters
    remainder = total_classes - (base_per_chapter * num_chapters)
    chapter_alloc = []
    for i, ch in enumerate(chapters):
        allocation = base_per_chapter + (1 if i < remainder else 0)
        chapter_alloc.append({'chapter': ch.get('title', f'Chapter {i+1}'), 'classes': allocation})

    # reserve last 15% for revision/tests
    revision_classes = ceil(total_classes * 0.15)
    test_classes = max(1, revision_classes // 3)

    # build weekly plan: assign chapters sequentially until classes exhausted
    weeklyPlan = []
    class_pointer = 0
    chapter_idx = 0
    remaining_classes = total_classes - revision_classes - test_classes
    week_start = s
    for w in range(total_weeks):
        week_classes = classesPerWeek
        if remaining_classes <= 0:
            week_assignment = []
        else:
            assign = min(week_classes, remaining_classes)
            week_assignment = []
            while assign > 0 and chapter_idx < len(chapter_alloc):
                ch_alloc = chapter_alloc[chapter_idx]
                available = ch_alloc['classes'] - class_pointer
                if available <= 0:
                    chapter_idx += 1
                    class_pointer = 0
                    continue
                take = min(assign, available)
                week_assignment.append({'chapter': ch_alloc['chapter'], 'classes': take})
                assign -= take
                class_pointer += take
                if class_pointer >= ch_alloc['classes']:
                    chapter_idx += 1
                    class_pointer = 0
        week_end = week_start + timedelta(days=6)
        weeklyPlan.append({'week': w+1, 'startDate': week_start.isoformat(), 'endDate': week_end.isoformat(), 'assignments': week_assignment})
        week_start = week_end + timedelta(days=1)

    doc = syllabus_plan_document(
        batchId=batchId,
        courseId=courseId,
        startDate=startDate,
        endDate=endDate,
        examDate=examDate,
        classesPerWeek=classesPerWeek,
        totalClasses=total_classes,
        revisionClasses=revision_classes,
        testClasses=test_classes,
        weeklyPlan=weeklyPlan,
        status='DRAFT',
        generatedBy=generatedBy,
    )

    res = await db.syllabus_plans.insert_one(doc)
    return str(res.inserted_id)


async def get_plan(planId: str):
    return await db.syllabus_plans.find_one({'_id': ObjectId(planId)})


async def approve_plan(planId: str, approverId: str):
    await db.syllabus_plans.update_one({'_id': ObjectId(planId)}, {'$set': {'status': 'APPROVED', 'approvedBy': approverId, 'approvedAt': datetime.utcnow()}})
    return True


async def list_plans_for_batch(batchId: str):
    items = []
    cursor = db.syllabus_plans.find({'batchId': batchId})
    async for p in cursor:
        p['id'] = str(p['_id'])
        items.append(p)
    return items
async def create_syllabus(plan: dict):
    # store plan in DB in real impl
    return {'id': 'demo'}

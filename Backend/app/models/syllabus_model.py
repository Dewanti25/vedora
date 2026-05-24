from datetime import datetime
from typing import List, Optional


def syllabus_plan_document(
    batchId: str,
    courseId: str,
    startDate: str,
    endDate: str,
    examDate: Optional[str],
    classesPerWeek: int,
    totalClasses: int,
    revisionClasses: int,
    testClasses: int,
    weeklyPlan: List[dict],
    status: str = 'DRAFT',
    generatedBy: str = 'AI',
):
    return {
        'batchId': batchId,
        'courseId': courseId,
        'startDate': startDate,
        'endDate': endDate,
        'examDate': examDate,
        'classesPerWeek': classesPerWeek,
        'totalClasses': totalClasses,
        'revisionClasses': revisionClasses,
        'testClasses': testClasses,
        'weeklyPlan': weeklyPlan,
        'status': status,
        'generatedBy': generatedBy,
        'createdAt': datetime.utcnow(),
    }

from datetime import datetime
from typing import List, Optional


def schedule_document(
    batchId: str,
    courseId: str,
    daysOfWeek: List[str],
    startTime: str,
    endTime: str,
    timezone: str = 'UTC',
    status: str = 'ACTIVE',
    createdBy: Optional[str] = None,
):
    return {
        'batchId': batchId,
        'courseId': courseId,
        'daysOfWeek': daysOfWeek,
        'startTime': startTime,
        'endTime': endTime,
        'timezone': timezone,
        'status': status,
        'createdBy': createdBy,
        'createdAt': datetime.utcnow(),
    }

import asyncio
import pytest

from app.services.batch_service import create_batch, join_batch_atomic
from app.database import connect_to_mongo, db, close_mongo_connection


@pytest.fixture(scope='module', autouse=True)
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop


@pytest.fixture(scope='module')
async def mongo():
    connect_to_mongo()
    yield
    # cleanup
    await db.batches.delete_many({})
    await db.enrollments.delete_many({})
    close_mongo_connection()


@pytest.mark.asyncio
async def test_concurrent_joins(mongo):
    # create a batch with max_students=3
    batch = {'name': 'test-batch', 'board': 'CBSE', 'class': '10', 'subject': 'Math', 'max': 3, 'students': 0}
    batch_id = await db.batches.insert_one(batch)
    batch_id = str(batch_id.inserted_id)

    # create 10 fake users
    users = [{'id': f'u{i}', 'email': f'user{i}@example.com'} for i in range(10)]

    async def join(u):
        return await join_batch_atomic(batch_id, u)

    results = await asyncio.gather(*[join(u) for u in users])
    enrolled = [r for r in results if r.get('status') == 'enrolled']
    assert len(enrolled) == 3

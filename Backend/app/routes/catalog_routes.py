from fastapi import APIRouter, Depends
from ..services.catalog_service import create_entity, list_entities
from ..deps import admin_required

router = APIRouter(prefix="/catalog", tags=["catalog"])


@router.post('/{collection}')
async def create_collection_item(collection: str, payload: dict, _=Depends(admin_required)):
    cid = await create_entity(collection, payload)
    return {'id': cid}


@router.get('/{collection}')
async def list_collection_items(collection: str):
    return await list_entities(collection)

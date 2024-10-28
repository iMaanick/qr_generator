from fastapi import APIRouter

from .index import index_router
from .qr import qr_router

root_router = APIRouter()
root_router.include_router(
    qr_router,
    prefix="/qr",
)
root_router.include_router(
    index_router,
)

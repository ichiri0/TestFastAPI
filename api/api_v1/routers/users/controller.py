from fastapi import APIRouter

from api.api_v1.routers.users.service import get_all_users, get_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/get-users")
async def read_tariff(tariff_id: int):
    return await get_user(tariff_id)


@router.get("/get-all-users")
async def read_all_tariffs():
    return await get_all_users()

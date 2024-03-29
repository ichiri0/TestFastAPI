from fastapi import APIRouter

from api.v1.routers.users.service import get_all_users, get_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/get-users")
async def read_user(user_id: int):
    return await get_user(user_id)


@router.get("/get-all-users")
async def read_all_users():
    return await get_all_users()

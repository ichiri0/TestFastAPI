from fastapi import APIRouter

from api.api_v1.routers.notes.service import get_note_by_id, get_notes_by_user_id

router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/get-note")
async def read_note(note_id: int):
    return await get_note_by_id(note_id)


@router.get("/get-note-by-user-id")
async def read_note_by_user_id(user_id: int):
    return await get_notes_by_user_id(user_id)

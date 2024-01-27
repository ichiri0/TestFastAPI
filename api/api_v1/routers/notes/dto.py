from typing import Optional
from pydantic import BaseModel


class NoteDTO(BaseModel):
    id: int
    user_id: int
    note: str
    is_completed: bool

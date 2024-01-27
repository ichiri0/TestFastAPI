from typing import Optional
from pydantic import BaseModel


class UserDTO(BaseModel):
    user_id: int
    first_name: Optional[str]
    last_name: Optional[str]

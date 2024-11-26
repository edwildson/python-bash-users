from typing import List
from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    folder: str
    numberMessages: int
    size: int


class GetUsersResponse(BaseModel):
    users: List[UserSchema]
    status: str
    status_code: int

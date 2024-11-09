from pydantic import BaseModel
from datetime import date
from uuid import UUID
from typing import List

class UserImageResponse(BaseModel):
    id: UUID
    image_url: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    birth_date: date

class UserResponse(UserCreate):
    id: UUID
    images: List[UserImageResponse] = []

    class Config:
        from_attributes = True

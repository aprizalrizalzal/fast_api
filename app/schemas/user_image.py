from pydantic import BaseModel
from uuid import UUID

class UserImageCreate(BaseModel):
    user_id: UUID
    image_url: str

class UserImageResponse(UserImageCreate):
    id: UUID

    class Config:
        from_attributes = True

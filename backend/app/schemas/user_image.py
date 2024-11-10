from pydantic import BaseModel
from uuid import UUID

# Skema untuk membuat user image baru
class UserImageCreate(BaseModel):
    user_id: UUID
    image_url: str

# Skema respons untuk menampilkan data user image
class UserImageResponse(UserImageCreate):
    id: UUID

    # Mengizinkan konversi dari objek SQLAlchemy
    class Config:
        from_attributes = True

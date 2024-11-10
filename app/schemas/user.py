from pydantic import BaseModel
from datetime import date
from uuid import UUID
from typing import List

# Skema respons untuk UserImage
class UserImageResponse(BaseModel):
    id: UUID
    image_url: str

    # Mengizinkan konversi dari objek SQLAlchemy
    class Config:
        from_attributes = True

# Skema untuk membuat user baru
class UserCreate(BaseModel):
    name: str
    birth_date: date

# Skema respons untuk user, termasuk daftar gambar pengguna
class UserResponse(UserCreate):
    id: UUID
    images: List[UserImageResponse] = []

    # Mengizinkan konversi dari objek SQLAlchemy
    class Config:
        from_attributes = True

import os
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from uuid import UUID
import shutil
from app.schemas.user_image import UserImageCreate, UserImageResponse
from app.crud.user_image import create_user_image, get_user_image, get_user_images, delete_user_image
from app.db.session import get_db

# Membuat router untuk endpoint user_image
router = APIRouter()

# Direktori untuk menyimpan file upload
if not os.path.exists("uploads"):
    os.makedirs("uploads")
    
# Endpoint untuk membuat gambar pengguna baru
@router.post("/", response_model=UserImageResponse)
def create_new_user_image(user_id: UUID, file: UploadFile = File(...), db: Session = Depends(get_db)):
     # Menyimpan file gambar yang diunggah ke folder 'uploads'
    image_path = f"uploads/{file.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Membuat instance UserImageCreate untuk gambar pengguna baru
    user_image = UserImageCreate(user_id=user_id, image_url=image_path)
    return create_user_image(db=db, user_image=user_image)

# Endpoint untuk membaca data gambar pengguna berdasarkan ID
@router.get("/{user_image_id}", response_model=UserImageResponse)
def read_user_image(user_image_id: UUID, db: Session = Depends(get_db)):
    db_user_image = get_user_image(db, user_image_id=user_image_id)
    if db_user_image is None:
        raise HTTPException(status_code=404, detail="User Image not found")
    return db_user_image

# Endpoint untuk membaca daftar gambar pengguna, mendukung pagination dengan skip dan limit
@router.get("/", response_model=list[UserImageResponse])
def read_user_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_user_images(db, skip=skip, limit=limit)

# Endpoint untuk menghapus gambar pengguna berdasarkan ID
@router.delete("/{user_image_id}", response_model=dict)
def delete_user_image_data(user_image_id: UUID, db: Session = Depends(get_db)):
    success = delete_user_image(db, user_image_id=user_image_id)
    if not success:
        raise HTTPException(status_code=404, detail="User Image not found")
    return {"detail": "User image deleted successfully"}

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from uuid import UUID
import shutil
import os
from app.schemas.user_image import UserImageCreate, UserImageResponse
from app.crud.user_image import create_user_image, get_user_image, get_user_images, update_user_image, delete_user_image
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=UserImageResponse)
def create_new_user_image(user_id: UUID, file: UploadFile = File(...), db: Session = Depends(get_db)):
    image_path = f"uploads/{file.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    user_image = UserImageCreate(user_id=user_id, image_url=image_path)
    return create_user_image(db=db, user_image=user_image)

@router.get("/{user_image_id}", response_model=UserImageResponse)
def read_user_image(user_image_id: UUID, db: Session = Depends(get_db)):
    db_user_image = get_user_image(db, user_image_id=user_image_id)
    if db_user_image is None:
        raise HTTPException(status_code=404, detail="User Image not found")
    return db_user_image

@router.get("/", response_model=list[UserImageResponse])
def read_user_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_user_images(db, skip=skip, limit=limit)

@router.put("/{user_image_id}", response_model=UserImageResponse)
def update_user_image_data(user_image_id: UUID, file: UploadFile = File(...), db: Session = Depends(get_db)):
    image_path = f"uploads/{file.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    db_user_image = update_user_image(db, user_image_id=user_image_id, image_url=image_path)
    if db_user_image is None:
        raise HTTPException(status_code=404, detail="User Image not found")
    return db_user_image

@router.delete("/{user_image_id}", response_model=dict)
def delete_user_image_data(user_image_id: UUID, db: Session = Depends(get_db)):
    success = delete_user_image(db, user_image_id=user_image_id)
    if not success:
        raise HTTPException(status_code=404, detail="User Image not found")
    return {"detail": "User image deleted successfully"}

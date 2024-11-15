from sqlalchemy.orm import Session
from uuid import UUID
from app.models.user_image import UserImage
from app.schemas.user_image import UserImageCreate

# Fungsi untuk membuat data user image baru
def create_user_image(db: Session, user_image: UserImageCreate):
    db_user_image = UserImage(user_id=user_image.user_id, image_url=user_image.image_url)
    db.add(db_user_image)
    db.commit()
    db.refresh(db_user_image)
    return db_user_image

# Fungsi untuk mengambil data user image berdasarkan ID
def get_user_image(db: Session, user_image_id: UUID):
    return db.query(UserImage).filter(UserImage.id == user_image_id).first()

# Fungsi untuk mengambil daftar user images dengan dukungan pagination
def get_user_images(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UserImage).offset(skip).limit(limit).all()

# Fungsi untuk menghapus data user image berdasarkan ID
def delete_user_image(db: Session, user_image_id: UUID):
    db_user_image = db.query(UserImage).filter(UserImage.id == user_image_id).first()
    if db_user_image:
        db.delete(db_user_image)
        db.commit()
        return True
    return False

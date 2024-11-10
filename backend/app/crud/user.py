from sqlalchemy.orm import Session
from uuid import UUID
from app.models.user import User
from app.schemas.user import UserCreate

# Fungsi untuk membuat data user baru
def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, birth_date=user.birth_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Fungsi untuk mengambil data user berdasarkan ID
def get_user(db: Session, user_id: UUID):
    return db.query(User).filter(User.id == user_id).first()

# Fungsi untuk mengambil daftar user dengan dukungan pagination
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# Fungsi untuk mengupdate data user berdasarkan ID
def update_user(db: Session, user_id: UUID, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.birth_date = user.birth_date
        db.commit()
        db.refresh(db_user)
    return db_user

# Fungsi untuk menghapus data user berdasarkan ID
def delete_user(db: Session, user_id: UUID):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

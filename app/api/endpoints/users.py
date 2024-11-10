from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user, get_user, get_users, update_user, delete_user
from app.db.session import get_db

# Membuat router untuk endpoint user
router = APIRouter()

# Endpoint untuk membuat pengguna baru
@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

# Endpoint untuk membaca data pengguna berdasarkan ID
@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Endpoint untuk membaca daftar pengguna, mendukung pagination dengan skip dan limit
@router.get("/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

# Endpoint untuk mengupdate pengguna berdasarkan ID
@router.put("/{user_id}", response_model=UserResponse)
def update_user_data(user_id: UUID, user: UserCreate, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Endpoint untuk menghapus gambar pengguna berdasarkan ID
@router.delete("/{user_id}", response_model=dict)
def delete_user_data(user_id: UUID, db: Session = Depends(get_db)):
    success = delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}

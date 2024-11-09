from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.endpoints import users, user_images
import os

# Membuat tabel di database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Menambahkan router untuk endpoint users dan user_images
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(user_images.router, prefix="/user_images", tags=["User Images"])

# Direktori untuk menyimpan file upload
if not os.path.exists("uploads"):
    os.makedirs("uploads")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.db.base import Base
from app.db.session import engine
from app.api.endpoints import users, user_images
import os
from fastapi.middleware.cors import CORSMiddleware

# Membuat tabel di database
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Menyajikan folder 'uploads' sebagai folder statis
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Menambahkan router untuk endpoint users dan user_images
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(user_images.router, prefix="/user_images", tags=["User Images"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

from datetime import date
import uuid
from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    birth_date = Column(Date, nullable=False)

    # Relasi dengan model UserImage (One to Many), satu pengguna bisa memiliki banyak gambar
    images = relationship("UserImage", back_populates="user")

    # Menambahkan properti untuk menghitung age secara dinamis
    @property
    def age(self):
        today = date.today()
        delta_years = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            delta_years -= 1
        return delta_years

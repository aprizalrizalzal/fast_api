import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class UserImage(Base):
    __tablename__ = "user_images"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    image_url = Column(String, nullable=False)

    # Relasi dengan model User (Many-to-One): Setiap gambar terkait dengan satu pengguna
    user = relationship("User", back_populates="images", cascade="save-update")

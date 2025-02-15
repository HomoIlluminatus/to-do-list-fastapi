from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import Column, UUID, String, DateTime, Enum
from sqlalchemy.orm import declarative_base

from entities.utils import Role, DcitUserMixin


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    
    id = Column(UUID, primary_key=True, default=uuid4)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )


class UserModel(BaseModel, DcitUserMixin):
    __tablename__ = 'users'
    
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(Role), nullable=False, default=Role.USER)
    
    def __str__(self):
        return f'{self.role}: {self.name}, e-mail: {self.email}'
    
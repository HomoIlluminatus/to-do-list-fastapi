from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr

from entities.utils import Role


class UserDTO(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    hashed_password: str
    role : Role
    created_at: datetime
    updated_at: datetime


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: Role
    created_at: datetime
    updated_at: datetime
    
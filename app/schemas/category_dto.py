from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
    
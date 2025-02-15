from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Union
from uuid import UUID, uuid4

from .utils import Role, DcitUserMixin
    
    
@dataclass
class BaseEntity(ABC):
    id: UUID = field(default_factory=uuid4, kw_only=True)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
        kw_only=True
    )
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
        kw_only=True
    )
    
    def update_time_stemp(self) -> None:
        self.updated_at = datetime.now(timezone.utc)


@dataclass
class User(BaseEntity, DcitUserMixin):
    name: str
    email: str
    hashed_password: str
    role: Role = field(default=Role.USER)
    
    def __post_init__(self) -> None:
        self.validate()
    
    def validate(self) -> None:
        ...
        
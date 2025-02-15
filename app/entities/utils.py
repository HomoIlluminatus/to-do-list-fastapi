from enum import Enum
from typing import Dict, Union
from uuid import UUID


class Role(Enum):
    USER = 'user'
    ADMIN = 'admin'


class DcitUserMixin:
    @property
    def user_dict(self) -> Dict[str, Union[UUID, str, Role]]:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'hashed_password': self.hashed_password,
            'role': self.role,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
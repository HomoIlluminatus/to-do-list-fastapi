from dataclasses import dataclass
from uuid import UUID

from .base_error import BaseAppError


@dataclass
class UserError(BaseAppError):
    @property
    def message(self) -> str:
        return "User error"


@dataclass
class UserNotFoundError(UserError):
    user_id: UUID = None
    email: str = None
    
    @property
    def message(self) -> str:
        if self.user_id is None and self.email is None:
            return f'User not found'
        if self.email is None:
            return f'User not found: id {self.user_id}'
        if self.user_id is None:
            return (
                f'There is no user with such an e-mail address:'
                f' {self.email}'
            )
        return f'user not found: id {self.user_id}, e-mail: {self.email}'
    
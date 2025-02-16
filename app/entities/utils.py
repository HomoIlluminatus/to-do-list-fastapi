from enum import Enum


class Role(Enum):
    USER = 'user'
    ADMIN = 'admin'
    

class TaskStatus(Enum):
    WAITING = 'waiting'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    
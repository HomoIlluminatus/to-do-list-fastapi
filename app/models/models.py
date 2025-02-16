from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import (
    Column,
    UUID,
    String,
    DateTime,
    Enum,
    Table,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base, relationship

from entities.utils import Role, TaskStatus


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    
    id = Column(UUID, primary_key=True, default=uuid4)
    created_at = Column(DateTime(timezone=True),
                        default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True),
                        default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))


class UserModel(BaseModel):
    __tablename__ = 'users'
    
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(Role), nullable=False, default=Role.USER)
    
    def __str__(self):
        return f'{self.role}: {self.name}, e-mail: {self.email}'


task_category_association = Table(
    'task_category_association',
    Base.metadata,
    Column('task_id', UUID, ForeignKey('tasks.id'), primary_key=True),
    Column('category_id', UUID, ForeignKey('categories.id'), primary_key=True)
)


class CategoryModel(BaseModel):
    __tablename__ = 'categories'
    
    user_id = Column(UUID, ForeignKey('users.id', ondelete='CASCADE'),
                     nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    
    tasks = relationship('TaskModel', secondary=task_category_association,
                         back_populates='categories', cascade='all, delete')
    
    def __str__(self):
        return f'category: {self.title}'
    

class TaskModel(BaseModel):
    __tablename__ = 'tasks'
    
    user = Column(UUID, ForeignKey('users.id', ondelete='CASCADE'),
                  nullable=False)
    category = Column(UUID, ForeignKey('categories.id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    deadline = Column(DateTime(timezone=True), nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.WAITING)
    
    categories = relationship('CategoryModel',
                               secondary=task_category_association,
                               back_populates='tasks', cascade='all, delete')
    
    def __str__(self):
        return f'task: {self.title}'
    
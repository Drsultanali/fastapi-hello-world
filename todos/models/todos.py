from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    is_completed: bool
   
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    


class UpdateTodo(SQLModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None
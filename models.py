from typing import Optional
from sqlmodel import SQLModel, Field

class TodoRead(SQLModel):
    id: int
    title: str
    description : Optional[str] = None
    done: bool = False

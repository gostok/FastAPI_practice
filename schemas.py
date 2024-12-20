from typing import Optional, Annotated
from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


class STaskID(BaseModel):
    ok: bool = True
    task_id: int

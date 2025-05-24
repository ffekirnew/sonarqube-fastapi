from typing import TypedDict


class Task(TypedDict):
    id: int
    description: str
    completed: bool

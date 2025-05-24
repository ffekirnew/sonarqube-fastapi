from typing import NotRequired, TypedDict


class UpdateTaskDto(TypedDict):
    description: NotRequired[str]
    completed: NotRequired[bool]

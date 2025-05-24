from abc import abstractmethod

from src.domain.dtos import CreateTaskDto, UpdateTaskDto
from src.domain.task import Task


class ABCTaskRepository:
    @abstractmethod
    def create_task(self, task_data: CreateTaskDto) -> Task: ...

    @abstractmethod
    def get_all(self) -> list[Task]: ...

    @abstractmethod
    def get(self, task_id: int) -> Task | None: ...

    @abstractmethod
    def delete_task(self, task_id: int) -> Task: ...

    @abstractmethod
    def update_task(self, task_id: int, task_data: UpdateTaskDto) -> Task: ...

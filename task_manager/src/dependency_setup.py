from src.domain.contracts.abc_task_repository import ABCTaskRepository
from src.infrastructure.task_repository import TaskRepository


def get_task_repository() -> ABCTaskRepository:
    return TaskRepository()

from src.common.exception import ApplicationException
from src.domain.dtos import CreateTaskDto, UpdateTaskDto
from src.infrastructure.task_repository import TaskRepository


def test_create_task():
    # Arrange
    repo = TaskRepository()
    task_data = CreateTaskDto(description="New Task")

    # Act
    task = repo.create_task(task_data)

    # Assert
    assert task["description"] == "New Task"
    assert not task["completed"]


def test_get_all_tasks():
    # Arrange
    repo = TaskRepository()

    # Act
    tasks = repo.get_all()

    # Assert
    assert len(tasks) >= 1  # At least the sample task exists


def test_get_task():
    # Arrange
    repo = TaskRepository()

    # Act
    task = repo.get(1000)  # Sample task ID

    # Assert
    assert task is not None
    assert task["description"] == "Sample task"


def test_get_nonexistent_task():
    # Arrange
    repo = TaskRepository()

    # Act
    task = repo.get(9999)

    # Assert
    assert task is None


def test_delete_task():
    # Arrange
    repo = TaskRepository()
    create_task_data = CreateTaskDto(description="Sample task")
    task_data = repo.create_task(create_task_data)

    # Act
    task = repo.delete_task(task_data["id"])

    # Assert
    assert task["description"] == "Sample task"
    assert repo.get(task_data["id"]) is None


def test_delete_nonexistent_task():
    # Arrange
    repo = TaskRepository()

    # Act & Assert
    try:
        repo.delete_task(9999)
    except ApplicationException:
        pass
    else:
        assert False, "Expected ApplicationException"


def test_update_task():
    # Arrange
    repo = TaskRepository()
    update_data = UpdateTaskDto(description="Updated Task", completed=True)

    # Act
    task = repo.update_task(1000, update_data)  # Sample task ID

    # Assert
    assert task["description"] == "Updated Task"
    assert task["completed"]


def test_update_nonexistent_task():
    # Arrange
    repo = TaskRepository()
    update_data = UpdateTaskDto(description="Updated Task", completed=True)

    # Act & Assert
    try:
        repo.update_task(9999, update_data)
    except ApplicationException:
        pass
    else:
        assert False, "Expected ApplicationException"

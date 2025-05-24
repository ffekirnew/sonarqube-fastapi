from typing import Annotated

from fastapi import Depends, FastAPI, Request
from src.common.exception import ApplicationException, Exceptions
from src.dependency_setup import get_task_repository
from src.domain.contracts import ABCTaskRepository
from src.domain.dtos import CreateTaskDto, UpdateTaskDto
from src.domain.responses.base_response import BaseResponse
from src.domain.task import Task
from starlette.responses import JSONResponse

# Initialize FastAPI application with metadata
Api = FastAPI(
    title="Task Management API",
    version="1.0.0",
    description="An example API for managing tasks. You can create, read, update, and delete tasks.",
)


@Api.get("/tasks/", tags=["Tasks"])
def get_all_tasks(
    task_repository: Annotated[ABCTaskRepository, Depends(get_task_repository)],
) -> BaseResponse[list[Task]]:
    tasks = task_repository.get_all()

    return BaseResponse[list[Task]].success(
        message="Tasks retrieved successfully.",
        data=tasks,
    )


@Api.post("/tasks/", tags=["Tasks"])
def create_task(
    create_task_dto: CreateTaskDto,
    task_repository: Annotated[ABCTaskRepository, Depends(get_task_repository)],
) -> BaseResponse[Task]:
    task = task_repository.create_task(create_task_dto)
    return BaseResponse[Task].success(
        message="Task created successfully.",
        data=task,
    )


@Api.get("/tasks/{task_id}", tags=["Tasks"])
def get_task(
    task_id: int,
    task_repository: Annotated[ABCTaskRepository, Depends(get_task_repository)],
) -> BaseResponse[Task]:
    task = task_repository.get(task_id)

    if task is None:
        raise ApplicationException(
            Exceptions.NotFoundException,
            "Cannot fetch task.",
            ["Task not found."],
        )

    return BaseResponse[Task].success(
        message="Task retrieved successfully.",
        data=task,
    )


@Api.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(
    task_id: int,
    update_task_dto: UpdateTaskDto,
    task_repository: Annotated[ABCTaskRepository, Depends(get_task_repository)],
) -> BaseResponse[Task]:
    updated_task = task_repository.update_task(task_id, update_task_dto)

    return BaseResponse[Task].success(
        message="Task updated successfully.",
        data=updated_task,
    )


@Api.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(
    task_id: int,
    task_repository: Annotated[ABCTaskRepository, Depends(get_task_repository)],
) -> BaseResponse[Task]:
    deleted_task = task_repository.delete_task(task_id)

    return BaseResponse[Task].success(
        message="Task deleted successfully.",
        data=deleted_task,
    )


@Api.exception_handler(ApplicationException)
async def application_exception_handler(
    request: Request, exception: ApplicationException
) -> JSONResponse:
    """
    Global exception handler for ApplicationException.
    Converts application-specific exceptions into appropriate JSON responses.
    
    Args:
        request (Request): The incoming request that caused the exception.
        exception (ApplicationException): The caught application exception.
        
    Returns:
        JSONResponse: A formatted error response with appropriate status code and error details.
    """
    return JSONResponse(
        status_code=exception.error_code,
        content=BaseResponse.error(
            message=exception.message,
            errors=exception.errors,
        ).to_dict(),
    )

import pytest
from pydantic import BaseModel

from clients.files.files_client import FilesClient, get_files_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from config import settings


class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user) -> FilesClient:
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file=settings.test_data.image_jpg_file)
    response = files_client.create_file(request=request)
    return FileFixture(request=request, response=response)

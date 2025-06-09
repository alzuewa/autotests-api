from pydantic import BaseModel, Field, FilePath, HttpUrl

from tools.fakers import fake


class FileSchema(BaseModel):
    """
    File structure
    """
    id: str
    filename: str | FilePath
    directory: str | FilePath
    url: HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Request structure to create file.
    """
    filename: str = Field(default_factory=lambda: f'{fake.uuid4()}.jpg')
    directory: str = Field(default='test_files')
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Creation file response structure.
    """
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    Getting file response structure.
    """
    file: FileSchema
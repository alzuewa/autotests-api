from pydantic import BaseModel, FilePath, HttpUrl, UUID4


class FileSchema(BaseModel):
    """
    File structure
    """
    id: UUID4
    filename: str | FilePath
    directory: str | FilePath
    url: HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Request structure to create file.
    """
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Creation file response structure.
    """
    file: FileSchema

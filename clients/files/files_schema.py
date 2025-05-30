from pydantic import BaseModel, FilePath, HttpUrl


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
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Creation file response structure.
    """
    file: FileSchema

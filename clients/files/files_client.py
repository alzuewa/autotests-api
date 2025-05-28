from pathlib import Path
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateFileRequestDict(TypedDict):
    """
    Request structure to create file.
    """
    filename: str
    directory: str
    upload_file: str | Path


class FilesClient(APIClient):
    """
    A client to work with /api/v1/files.
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Method to get file by its id.
        :param file_id: id of the file.
        :return: Response object of type httpx.Response.
        """
        return self.get(f'/api/v1/files/{file_id}')

    def post_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Method to upload file.
        :param request: a dict with `filename`, `directory`, `upload_file`.
        :return: Response object of type httpx.Response.
        """
        return self.post(
            '/api/v1/files',
            data=request,  # It's OK that `upload_file` will also be passed here (as unused field)
            files={'upload_file': open(f'testdata/files/{request["upload_file"]}')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Method to delete file by its id.
        :param file_id: id of the file.
        :return: Response object of type httpx.Response.
        """
        return self.delete(f'/api/v1/files/{file_id}')

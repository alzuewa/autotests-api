import allure
from httpx import Response

from clients.api_client import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class FilesClient(APIClient):
    """
    A client to work with /api/v1/files.
    """

    @allure.step('Get file by id {file_id}')
    def get_file_api(self, file_id: str) -> Response:
        """
        Method to get file by its id.
        :param file_id: id of the file.
        :return: Response object of type httpx.Response.
        """
        return self.get(f'/api/v1/files/{file_id}')

    @allure.step('Create file')
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Method to upload file.
        :param request: a dict with `filename`, `directory`, `upload_file`.
        :return: Response object of type httpx.Response.
        """
        # `files` param is passed not as `files={'upload_file': open(f'{request.upload_file}', 'rb')}`
        # due to changing `upload_file` type to pydantic.FilePath. It requires read_bytes()
        return self.post(
            '/api/v1/files',
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={'upload_file': request.upload_file.read_bytes()}
        )

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)

    @allure.step('Delete file by id {file_id}')
    def delete_file_api(self, file_id: str) -> Response:
        """
        Method to delete file by its id.
        :param file_id: id of the file.
        :return: Response object of type httpx.Response.
        """
        return self.delete(f'/api/v1/files/{file_id}')


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Function which creates FilesClient instance as HTTP-client with full setup.
    :param user: AuthenticationUserSchema object with user email and password.
    :return: Ready-to-use FilesClient object.
    """
    client = get_private_http_client(user)
    return FilesClient(client)

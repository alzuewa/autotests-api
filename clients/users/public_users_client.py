import allure
from httpx import Response

from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.routes import APIRoutes


class PublicUsersClient(APIClient):
    """
    A client to work with /api/v1/users without auth.
    """

    @allure.step('Create user')
    @tracker.track_coverage_httpx(APIRoutes.USERS)
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Creates a new user.
        :param request: a dict with `email`, `password`, `lastName`, `firstName`, `middleName`.
        :return: Response object of type httpx.Response.
        """
        return self.post(APIRoutes.USERS, json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Function which creates PublicUsersClient instance as HTTP-client with full setup.
    :return: Ready-to-use PublicUsersClient object.
    """
    client = get_public_http_client()
    return PublicUsersClient(client=client)

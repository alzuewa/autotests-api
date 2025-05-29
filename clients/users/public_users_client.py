from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
    """
    Request structure to create user.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    A client to work with /api/v1/users without auth.
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Creates a new user.
        :param request: a dict with `email`, `password`, `lastName`, `firstName`, `middleName`.
        :return: Response object of type httpx.Response.
        """
        return self.post('/api/v1/users', json=request)


def get_public_users_client() -> PublicUsersClient:
    """
    Function which creates PublicUsersClient instance as HTTP-client with full setup.
    :return: Ready-to-use PublicUsersClient object.
    """
    client = get_public_http_client()
    return PublicUsersClient(client=client)

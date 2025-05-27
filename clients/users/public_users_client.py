from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


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
        :return: Response object with response data.
        """
        return self.post('/api/v1/users', json=request)

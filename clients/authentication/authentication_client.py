from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class LoginRequestDict(TypedDict):
    """
    Request structure for authentication.
    """
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """
    Request structure for accessToken renew.
    """
    refreshToken: str


class AuthenticationClient(APIClient):
    """
    A client to work with /api/v1/authentication.
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Performs user authentication.
        :param request: a dict with `email` and `password`.
        :return: Response object with response data.
        """
        return self.post('/api/v1/authentication/login', json=request)

    def refresh_api(self, request: RefreshRequestDict):
        """
        Renews accessToken.
        :param request: a dict with `refreshToken`.
        :return: Response object with response data.
        """
        return self.post('/api/v1/authentication/refresh', json=request)

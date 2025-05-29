from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginRequestDict(TypedDict):
    """
    Request structure for authentication.
    """
    email: str
    password: str


class LoginResponseDict(TypedDict):
    token: Token


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
        :return: Response object of type httpx.Response.
        """
        return self.post('/api/v1/authentication/login', json=request)

    def refresh_api(self, request: RefreshRequestDict):
        """
        Renews accessToken.
        :param request: a dict with `refreshToken`.
        :return: Response object of type httpx.Response.
        """
        return self.post('/api/v1/authentication/refresh', json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        Performs user authentication.
        :param request: a dict with `email` and `password`.
        :return: Response object of type LoginResponseDict, i.e. response in the form of JSON.
        """
        response = self.login_api(request)
        return response.json()


def get_authentication_client() -> AuthenticationClient:
    """
    Function which creates AuthenticationClient instance as HTTP-client with full setup.
    :return: Ready-to-use AuthenticationClient object.
    """
    client = get_public_http_client()
    return AuthenticationClient(client=client)

import allure
from httpx import Response

from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema
from clients.public_http_builder import get_public_http_client
from tools.routes import APIRoutes


class AuthenticationClient(APIClient):
    """
    A client to work with /api/v1/authentication.
    """

    @allure.step('Authenticate user')
    @tracker.track_coverage_httpx(f'{APIRoutes.AUTHENTICATION}/login')
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Performs user authentication.
        :param request: a dict with `email` and `password`.
        :return: Response object of type httpx.Response.
        """
        return self.post(f'{APIRoutes.AUTHENTICATION}/login', json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

    @allure.step('Refresh authentication token')
    @tracker.track_coverage_httpx(f'{APIRoutes.AUTHENTICATION}/refresh')
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Renews accessToken.
        :param request: a dict with `refreshToken`.
        :return: Response object of type httpx.Response.
        """
        return self.post(f'{APIRoutes.AUTHENTICATION}/refresh', json=request.model_dump(by_alias=True))


def get_authentication_client() -> AuthenticationClient:
    """
    Function which creates AuthenticationClient instance as HTTP-client with full setup.
    :return: Ready-to-use AuthenticationClient object.
    """
    client = get_public_http_client()
    return AuthenticationClient(client=client)

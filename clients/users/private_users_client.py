from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema


class PrivateUsersClient(APIClient):
    """
    A client to work with /api/v1/users with auth.
    """

    def get_user_me_api(self) -> Response:
        """
        Method to get current user.
        :return: Response object of type httpx.Response.
        """
        return self.get('/api/v1/users/me')

    def get_user_api(self, user_id: str) -> Response:
        """
        Method to get user by its id.
        :param user_id: id of the user.
        :return: Response object of type httpx.Response.
        """
        return self.get(f'/api/v1/users/{user_id}')

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Method to update user by its id.
        :param user_id: id of the user.
        :param request: a dict with `email`, `lastName`, `firstName`, `middleName`.
        :return: Response object of type httpx.Response.
        """
        return self.patch(f'/api/v1/users/{user_id}', json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Method to delete user by its id.
        :param user_id: id of the user.
        :return: Response object of type httpx.Response.
        """
        return self.delete(f'/api/v1/users/{user_id}')


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Function which creates PrivateUsersClient instance as HTTP-client with full setup.
    :param user: AuthenticationUserSchema object with user email and password.
    :return: Ready-to-use PrivateUsersClient object.
    """
    client = get_private_http_client(user)
    return PrivateUsersClient(client)

from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class UpdateUserRequestDict(TypedDict):
    """
    Request structure to update user.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


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

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Method to update user by its id.
        :param user_id: id of the user.
        :param request: a dict with `email`, `lastName`, `firstName`, `middleName`.
        :return: Response object of type httpx.Response.
        """
        return self.patch(f'/api/v1/users/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Method to delete user by its id.
        :param user_id: id of the user.
        :return: Response object of type httpx.Response.
        """
        return self.delete(f'/api/v1/users/{user_id}')

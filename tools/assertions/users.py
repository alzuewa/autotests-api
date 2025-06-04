from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(
        response: CreateUserResponseSchema,
        request: CreateUserRequestSchema
) -> None | AssertionError:
    """
    Checks that CreateUserRequest matches CreateUserResponse
    :param response: API response with user data
    :param request: Initial request to create user
    :return: None
    :raises: AssertionError if request and response don't match
    """
    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.last_name, request.last_name, 'last_name')
    assert_equal(response.user.first_name, request.first_name, 'first_name')
    assert_equal(response.user.middle_name, request.middle_name, 'middle_name')
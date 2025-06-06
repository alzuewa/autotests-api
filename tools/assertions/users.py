from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
    UserSchema
)

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


def assert_user(actual: UserSchema, expected: UserSchema) -> None | AssertionError:
    """
    Checks that actual user data matches expected
    :param actual: actual user data
    :param expected: expected user data
    :return: None
    :raises: AssertionError if actual and expected data don't match
    """
    assert_equal(actual.id, expected.id, name='id')
    assert_equal(actual.email, expected.email, name='email')
    assert_equal(actual.last_name, expected.last_name, name='last_name')
    assert_equal(actual.first_name, expected.first_name, name='first_name')
    assert_equal(actual.middle_name, expected.middle_name, name='middle_name')


def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
) -> None | AssertionError:
    """
    Checks that response for getting user matches response for its creating
    :param get_user_response: API response for getting user data
    :param create_user_response: API response for creating user data
    :return: None
    :raises: AssertionError if getting and creating user data don't match
    """
    return assert_user(actual=get_user_response.user, expected=create_user_response.user)

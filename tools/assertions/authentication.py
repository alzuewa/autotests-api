import allure

from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true
from tools.logger import get_logger

logger = get_logger('AUTH_ASSERTIONS')


@allure.step('Check login user response')
def assert_login_response(response: LoginResponseSchema) -> None:
    """
    Checks LoginResponse on successful authentication
    :param response: API response with token data
    :return: None
    :raises: AssertionError if request and response don't match
    """
    logger.info('Check login user response')

    assert_equal(response.token.token_type, 'bearer', 'token_type')
    assert_is_true(response.token.access_token, 'access_token')
    assert_is_true(response.token.refresh_token, 'refresh_token')

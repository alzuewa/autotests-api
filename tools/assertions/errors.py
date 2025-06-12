import allure

from clients.errors_schema import ClientErrorResponseSchema, ValidationErrorSchema, ValidationErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger

logger = get_logger('ERRORS_ASSERTIONS')


@allure.step('Check validation error')
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema) -> None:
    """
    Checks that actual ValidationErrorSchema matches expected one
    :param actual: Actual ValidationErrorSchema
    :param expected: Expected ValidationErrorSchema
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
    logger.info('Check validation error')

    assert_equal(actual.type, expected.type, name='type')
    assert_equal(actual.input, expected.input, name='input')
    assert_equal(actual.context, expected.context, name='context')
    assert_equal(actual.message, expected.message, name='message')
    assert_equal(actual.location, expected.location, name='location')


@allure.step('Check validation error response')
def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
) -> None:
    """
    Checks that actual ValidationErrorResponse matches expected one
    :param actual: Actual ValidationErrorResponseSchema
    :param expected: Expected ValidationErrorResponseSchema
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
    logger.info('Check validation error response')

    assert_length(actual.details, expected.details, name='details')

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


@allure.step('Check client error response')
def assert_client_error_response(
        actual: ClientErrorResponseSchema,
        expected: ClientErrorResponseSchema
) -> None:
    """
    Checks that actual ClientErrorResponse matches expected one
    :param actual: Actual ClientErrorResponseSchema
    :param expected: Expected ClientErrorResponseSchema
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
    logger.info('Check client error response')

    assert_equal(actual.details, expected.details, name='details')

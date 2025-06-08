from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length


def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema) -> None | AssertionError:
    """
    Checks that actual ValidationErrorSchema matches expected one
    :param actual: Actual ValidationErrorSchema
    :param expected: Expected ValidationErrorSchema
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
    assert_equal(actual.type, expected.type, name='type')
    assert_equal(actual.input, expected.input, name='input')
    assert_equal(actual.context, expected.context, name='context')
    assert_equal(actual.message, expected.message, name='message')
    assert_equal(actual.location, expected.location, name='location')

def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
) -> None | AssertionError:
    """
    Checks that actual ValidationErrorResponse matches expected one
    :param actual: Actual ValidationErrorResponseSchema
    :param expected: Expected ValidationErrorResponseSchema
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
    assert_length(actual.details, expected.details, name='details')

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


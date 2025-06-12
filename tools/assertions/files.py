import allure

from clients.errors_schema import ClientErrorResponseSchema, ValidationErrorResponseSchema, ValidationErrorSchema
from clients.files.files_schema import (
    CreateFileRequestSchema,
    CreateFileResponseSchema,
    FileSchema,
    GetFileResponseSchema,
)
from config import settings
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_client_error_response, assert_validation_error_response
from tools.logger import get_logger

logger = get_logger('FILES_ASSERTIONS')


@allure.step('Check create file response')
def assert_create_file_response(
        response: CreateFileResponseSchema,
        request: CreateFileRequestSchema
) -> None:
    """
   Checks that CreateFileRequest matches CreateFileResponse
   :param response: actual file data
   :param request: expected file data
   :return: None
   :raises: AssertionError if actual and expected data don't match
   """
    logger.info('Check create file response')

    # No slash before `static`: pydantic.HttpUrl automatically adds trailing slash if it's absent
    expected_url = f'{settings.http_client.client_url}static/{request.directory}/{request.filename}'

    assert_equal(response.file.filename, request.filename, name='filename')
    assert_equal(response.file.directory, request.directory, name='directory')
    assert_equal(str(response.file.url), expected_url, name='url')


@allure.step('Check create file')
def assert_file(actual: FileSchema, expected: FileSchema) -> None:
    """
    Checks that actual file data matches expected
    :param actual: actual file data
    :param expected: expected file data
    :return: None
    :raises: AssertionError if actual and expected data don't match
    """
    logger.info('Check create file')

    assert_equal(actual.id, expected.id, name='id')
    assert_equal(actual.url, expected.url, name='url')
    assert_equal(actual.filename, expected.filename, name='filename')
    assert_equal(actual.directory, expected.directory, name='directory')


@allure.step('Check get file response')
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
) -> None:
    """
    Checks that GetFileResponse matches CreateFileResponse
    :param get_file_response: API response to get file
    :param create_file_response: API response to create file
    :return: None
    :raises: AssertionError if getting and creating file data don't match
    """
    logger.info('Check get file response')

    assert_file(get_file_response.file, create_file_response.file)


@allure.step('Check create file with empty filename response')
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema) -> None:
    """
    Checks that API response to creating a file with empty filename matches expected Validation error
    :param actual: API response with Validation error which needs to be checked
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
    logger.info('Check create file with empty filename response')

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='string_too_short',
                input='',
                context={'min_length': 1},
                message='String should have at least 1 character',
                location=['body', 'filename']
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step('Check create file with empty directory response')
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema) -> None:
    """
    Checks that API response to creating a file with empty directory matches expected Validation error
    :param actual: API response with Validation error which needs to be checked
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
    logger.info('Check create file with empty directory response')

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='string_too_short',
                input='',
                context={'min_length': 1},
                message='String should have at least 1 character',
                location=['body', 'directory']
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step('Check file not found response')
def assert_file_not_found_response(actual: ClientErrorResponseSchema) -> None:
    """
    Checks that actual error response matches expected
    :param actual: actual response
    :return: None
    :raises: AssertionError if actual and expected data don't match
    """
    logger.info('Check file not found response')

    expected = ClientErrorResponseSchema(details='File not found')
    assert_client_error_response(actual, expected)


@allure.step('Check create file with incorrect file id response')
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema) -> None:
    """
    Checks that API response to getting a file with invalid file ID matches expected Validation error
    :param actual: API response with Validation error which needs to be checked
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
    logger.info('Check create file with incorrect file id response')

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type='uuid_parsing',
                input='incorrect-file-id',
                context={'error': 'invalid character: expected an optional prefix of `urn:uuid:` '
                                  'followed by [0-9a-fA-F-], found `i` at 1'
                         },
                message='Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` '
                        'followed by [0-9a-fA-F-], found `i` at 1',
                location=['path', 'file_id']
            )
        ]
    )
    assert_validation_error_response(actual, expected)

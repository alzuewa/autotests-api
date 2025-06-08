from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema
from clients.files.files_schema import (
    CreateFileRequestSchema,
    CreateFileResponseSchema,
    FileSchema,
    GetFileResponseSchema,
)
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response


def assert_create_file_response(
        response: CreateFileResponseSchema,
        request: CreateFileRequestSchema
) -> None | AssertionError:
    """
   Checks that CreateFileRequest matches CreateFileResponse
   :param response: actual file data
   :param request: expected file data
   :return: None
   :raises: AssertionError if actual and expected data don't match
   """
    expected_url = f'http://localhost:8000/static/{request.directory}/{request.filename}'

    assert_equal(response.file.filename, request.filename, name='filename')
    assert_equal(response.file.directory, request.directory, name='directory')
    assert_equal(str(response.file.url), expected_url, name='url')


def assert_file(actual: FileSchema, expected: FileSchema) -> None | AssertionError:
    """
    Checks that actual file data matches expected
    :param actual: actual file data
    :param expected: expected file data
    :return: None
    :raises: AssertionError if actual and expected data don't match
    """
    assert_equal(actual.id, expected.id, name='id')
    assert_equal(actual.url, expected.url, name='url')
    assert_equal(actual.filename, expected.filename, name='filename')
    assert_equal(actual.directory, expected.directory, name='directory')


def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
) -> None | AssertionError:
    """
    Checks that GetFileResponse matches CreateFileResponse
    :param get_file_response: API response to get file
    :param create_file_response: API response to create file
    :return: None
    :raises: AssertionError if getting and creating file data don't match
    """
    assert_file(get_file_response.file, create_file_response.file)

def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema) -> None | AssertionError:
    """
    Checks that API response to creating file with empty filename matches expected Validation error
    :param actual: API response with Validation error which needs to be checked
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
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

def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema) -> None | AssertionError:
    """
    Checks that API response to creating file with empty directory matches expected Validation error
    :param actual: API response with Validation error which needs to be checked
    :return: None
    :raises: AssertionError if actual response doesn't match expected one
    """
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
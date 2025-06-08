from http import HTTPStatus

import pytest

from clients.errors_schema import ValidationErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.files import (
    assert_create_file_response,
    assert_create_file_with_empty_directory_response,
    assert_create_file_with_empty_filename_response,
    assert_get_file_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.files
@pytest.mark.regression
class TestFiles:

    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file='testdata/files/image.jpg')
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(response_data, request)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_get_file(self, files_client: FilesClient, function_file):
        file_id = function_file.response.file.id
        response = files_client.get_file_api(file_id=file_id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(filename='', upload_file='testdata/files/image.jpg')
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(directory='', upload_file='testdata/files/image.jpg')
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
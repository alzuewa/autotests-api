from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import (
    GetCoursesQuerySchema,
    GetCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema
)
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:

    def test_get_courses(self, courses_client: CoursesClient, function_course: CourseFixture):
        query = GetCoursesQuerySchema(user_id=function_course.request.created_by_user_id)
        response = courses_client.get_courses_api(query=query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        course_id = function_course.response.course.id

        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(course_id=course_id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(response_data, request)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.assertions.base import assert_equal


def assert_update_course_response(
        response: UpdateCourseResponseSchema,
        request: UpdateCourseRequestSchema
) -> None | AssertionError:
    """
    Checks that UpdateCourseResponse matches UpdateCourseRequest
    :param response: API response to update course data
    :param request: Request to update course data
    :return: None
    :raises: AssertionError if request and response to update course don't match
    """
    assert_equal(response.course.title, request.title, name='title')
    assert_equal(response.course.max_score, request.max_score, name='max_score')
    assert_equal(response.course.min_score, request.min_score, name='min_score')
    assert_equal(response.course.description, request.description, name='description')
    assert_equal(response.course.estimated_time, request.estimated_time, name='estimated_time')

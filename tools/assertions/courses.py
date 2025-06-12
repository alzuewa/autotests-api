import allure

from clients.courses.courses_schema import (
    CourseSchema,
    CreateCourseResponseSchema,
    CreateCourseRequestSchema,
    GetCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema
)
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
from tools.logger import get_logger

logger = get_logger('COURSES_ASSERTIONS')


@allure.step('Check course')
def assert_course(actual: CourseSchema, expected: CourseSchema) -> None:
    """
    Checks that actual course data matches expected one
    :param actual: Actual course data
    :param expected: Expected course data
    :return: None
    :raises: AssertionError if actual and expected course data don't match
    """
    logger.info('Check course')

    assert_equal(actual.id, expected.id, name='id')
    assert_equal(actual.title, expected.title, name='title')
    assert_equal(actual.max_score, expected.max_score, name='max_score')
    assert_equal(actual.min_score, expected.min_score, name='min_score')
    assert_equal(actual.description, expected.description, name='description')
    assert_equal(actual.estimated_time, expected.estimated_time, name='estimated_time')

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


@allure.step('Check get courses response')
def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
) -> None:
    """
    Checks that GetCoursesResponse matches a list of created courses
    :param get_courses_response: API response to get a courses list
    :param create_course_responses: A list of API responses to create courses
    :return: None
    :raises: AssertionError if response to get courses and response to create courses don't match
    """
    logger.info('Check get courses response')

    assert_length(get_courses_response.courses, create_course_responses, name='courses')

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)


@allure.step('Check create course response')
def assert_create_course_response(
        response: CreateCourseResponseSchema,
        request: CreateCourseRequestSchema
) -> None:
    """
    Checks that CreateCourseResponse matches CreateCourseRequest
    :param response: API response with course data
    :param request: Initial request to create course
    :return: None
    :raises: AssertionError if request and response don't match
    """
    logger.info('Check create course response')

    assert_equal(response.course.title, request.title, name='title')
    assert_equal(response.course.max_score, request.max_score, name='max_score')
    assert_equal(response.course.min_score, request.min_score, name='min_score')
    assert_equal(response.course.description, request.description, name='description')
    assert_equal(response.course.estimated_time, request.estimated_time, name='estimated_time')
    assert_equal(response.course.estimated_time, request.estimated_time, name='estimated_time')
    assert_equal(response.course.preview_file.id, request.preview_file_id, name='preview_file')
    assert_equal(response.course.created_by_user.id, request.created_by_user_id, name='created_by_user')


@allure.step('Check update course response')
def assert_update_course_response(
        response: UpdateCourseResponseSchema,
        request: UpdateCourseRequestSchema
) -> None:
    """
    Checks that UpdateCourseResponse matches UpdateCourseRequest
    :param response: API response to update course data
    :param request: Request to update course data
    :return: None
    :raises: AssertionError if request and response to update course don't match
    """
    logger.info('Check update course response')

    # Only all course fields update is currently applicable, so conditional checks aren't mandatory
    if request.title is not None:
        assert_equal(response.course.title, request.title, name='title')
    if request.max_score is not None:
        assert_equal(response.course.max_score, request.max_score, name='max_score')
    if request.min_score is not None:
        assert_equal(response.course.min_score, request.min_score, name='min_score')
    if request.description is not None:
        assert_equal(response.course.description, request.description, name='description')
    if request.estimated_time is not None:
        assert_equal(response.course.estimated_time, request.estimated_time, name='estimated_time')

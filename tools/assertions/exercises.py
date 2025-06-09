from clients.errors_schema import ClientErrorResponseSchema
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    ExerciseSchema,
    GetExerciseResponseSchema,
    GetExercisesListResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_client_error_response


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema) -> None:
    """
    Checks that actual exercise data matches expected one
    :param actual: Actual exercise data
    :param expected: Expected exercise data
    :return: None
    :raises: AssertionError if actual and expected exercise data don't match
    """
    assert_equal(actual.id, expected.id, name='id')
    assert_equal(actual.title, expected.title, name='title')
    assert_equal(actual.course_id, expected.course_id, name='course_id')
    assert_equal(actual.max_score, expected.max_score, name='max_score')
    assert_equal(actual.min_score, expected.min_score, name='min_score')
    assert_equal(actual.order_index, expected.order_index, name='order_index')
    assert_equal(actual.description, expected.description, name='description')
    assert_equal(actual.estimated_time, expected.estimated_time, name='estimated_time')


def assert_create_exercise_response(
        response: CreateExerciseResponseSchema,
        request: CreateExerciseRequestSchema
) -> None:
    """
    Checks that CreateExerciseResponse matches CreateExerciseRequest
    :param response: API response with exercise data
    :param request: Initial request to create exercise
    :return: None
    :raises: AssertionError if request and response don't match
    """
    assert_equal(response.exercise.title, request.title, name='title')
    assert_equal(response.exercise.course_id, request.course_id, name='course_id')
    assert_equal(response.exercise.max_score, request.max_score, name='max_score')
    assert_equal(response.exercise.min_score, request.min_score, name='min_score')
    assert_equal(response.exercise.order_index, request.order_index, name='order_index')
    assert_equal(response.exercise.description, request.description, name='description')
    assert_equal(response.exercise.estimated_time, request.estimated_time, name='estimated_time')


def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
) -> None:
    """
    Checks that GetExerciseResponse matches CreateExerciseResponse
    :param get_exercise_response: API response to get exercise data
    :param create_exercise_response: API response to create exercise
    :return: None
    :raises: AssertionError if getting and creating exercise response data don't match
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


def assert_update_exercise_response(
        response: UpdateExerciseResponseSchema,
        request: UpdateExerciseRequestSchema
) -> None:
    """
    Checks that UpdateExerciseResponse matches UpdateExerciseRequest
    :param response: API response to update exercise data
    :param request: Request to update exercise data
    :return: None
    :raises: AssertionError if request and response to update exercise don't match
    """
    assert_equal(response.exercise.title, request.title, name='title')
    assert_equal(response.exercise.max_score, request.max_score, name='max_score')
    assert_equal(response.exercise.min_score, request.min_score, name='min_score')
    assert_equal(response.exercise.order_index, request.order_index, name='order_index')
    assert_equal(response.exercise.description, request.description, name='description')
    assert_equal(response.exercise.estimated_time, request.estimated_time, name='estimated_time')


def assert_exercise_not_found_response(actual: ClientErrorResponseSchema) -> None:
    """
    Checks that actual error response matches expected
    :param actual: actual response
    :return: None
    :raises: AssertionError if actual and expected data don't match
    """
    expected = ClientErrorResponseSchema(details='Exercise not found')
    assert_client_error_response(actual, expected)


def assert_get_exercises_response(
        get_exercises_response: GetExercisesListResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
) -> None:
    """
    Checks that GetExercisesListResponse matches a list of created exercises
    :param get_exercises_response: API response to get an exercises list
    :param create_exercise_responses: A list of API responses to create exercise
    :return: None
    :raises: AssertionError if response to get exercises and response to create exercises don't match
    """
    assert_length(get_exercises_response.exercises, create_exercise_responses, name='exercises')

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)

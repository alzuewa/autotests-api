from http import HTTPStatus

import allure
import pytest

from clients.errors_schema import ClientErrorResponseSchema
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExercisesListResponseSchema,
    GetExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response,
    assert_exercise_not_found_response,
    assert_get_exercise_response,
    assert_get_exercises_response,
    assert_update_exercise_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
class TestExercises:

    @allure.title('Create exercise')
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    def test_create_exercise(self, exercises_client, function_course):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request=request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(response_data, request)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title('Get exercise')
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    def test_get_exercise(self, exercises_client, function_exercise):
        exercise_id = function_exercise.response.exercise.id

        response = exercises_client.get_exercise_api(exercise_id=exercise_id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title('Update exercise')
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    def test_update_exercise(self, exercises_client, function_exercise):
        exercise_id = function_exercise.response.exercise.id

        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(exercise_id=exercise_id, request=request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(response_data, request)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title('Delete exercise')
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    def test_delete_exercise(self, exercises_client, function_exercise):
        exercise_id = function_exercise.response.exercise.id

        delete_response = exercises_client.delete_exercise_api(exercise_id=exercise_id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(exercise_id=exercise_id)
        get_response_data = ClientErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(instance=get_response.json(), schema=get_response_data.model_json_schema())

    @allure.title('Get exercises')
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    def test_get_exercises(self, exercises_client, function_exercise):
        query = GetExercisesQuerySchema(course_id=function_exercise.request.course_id)

        response = exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesListResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

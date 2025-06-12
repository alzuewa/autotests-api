import allure
from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExerciseResponseSchema,
    GetExercisesListResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    A client to work with /api/v1/exercises.
    """

    @allure.step('Get exercises')
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Method to get all exercises in course with id `courseId`.
        :param query: a dict with `courseId`.
        :return: Response object of type httpx.Response.
        """
        return self.get(APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))  # noqa

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesListResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesListResponseSchema.model_validate_json(response.text)

    @allure.step('Get exercise with exercise id {exercise_id}')
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Method to get exercise by its id.
        :param exercise_id: id of the exercise.
        :return: Response object of type httpx.Response.
        """
        return self.get(f'{APIRoutes.EXERCISES}/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    @allure.step('Create exercise')
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Method to create exercise.
        :param request: a dict with `title`, `courseId`, `maxScore`, `minScore`, `orderIndex`,
        `description`, `estimatedTime`.
        :return: Response object of type httpx.Response.
        """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    @allure.step('Update exercise with exercise id {exercise_id}')
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Method to update exercise by its id.
        :param exercise_id: id of the exercise.
        :param request: a dict with `title`, `maxScore`, `minScore`, `orderIndex`, `description`, `estimatedTime`.
        :return: Response object of type httpx.Response.
        """
        return self.patch(f'{APIRoutes.EXERCISES}/{exercise_id}', json=request.model_dump(by_alias=True))

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    @allure.step('Delete exercise with exercise id {exercise_id}')
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Method to delete exercise by its id.
        :param exercise_id: id of the exercise.
        :return: Response object of type httpx.Response.
        """
        return self.delete(f'{APIRoutes.EXERCISES}/{exercise_id}')


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Function which creates ExercisesClient instance as HTTP-client with full setup.
    :param user: AuthenticationUserSchema object with user email and password.
    :return: Ready-to-use ExercisesClient object.
    """
    client = get_private_http_client(user)
    return ExercisesClient(client)

from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class Exercise(TypedDict):
    """
    Exercise structure
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Request structure to get an exercises list.
    """
    courseId: str


class GetExerciseResponseDict(TypedDict):
    """
    Getting exercise response structure.
    """
    exercise: Exercise


class GetExercisesListResponseDict(TypedDict):
    """
    Getting exercises list response structure.
    """
    exercises: list[Exercise]


class CreateExerciseRequestDict(TypedDict):
    """
    Request structure to create exercise.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Creating exercise response structure.
    """
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Request structure to update exercise.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """
    Updating exercise response structure.
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    A client to work with /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Method to get all exercises in course with id `courseId`.
        :param query: a dict with `courseId`.
        :return: Response object of type httpx.Response.
        """
        return self.get('/api/v1/exercises', params=query)  # noqa

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesListResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Method to get exercise by its id.
        :param exercise_id: id of the exercise.
        :return: Response object of type httpx.Response.
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Method to create exercise.
        :param request: a dict with `title`, `courseId`, `maxScore`, `minScore`, `orderIndex`,
        `description`, `estimatedTime`.
        :return: Response object of type httpx.Response.
        """
        return self.post('/api/v1/exercises', json=request)

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Method to update exercise by its id.
        :param exercise_id: id of the exercise.
        :param request: a dict with `title`, `maxScore`, `minScore`, `orderIndex`, `description`, `estimatedTime`.
        :return: Response object of type httpx.Response.
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Method to delete exercise by its id.
        :param exercise_id: id of the exercise.
        :return: Response object of type httpx.Response.
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Function which creates ExercisesClient instance as HTTP-client with full setup.
    :param user: AuthenticationUserSchema object with user email and password.
    :return: Ready-to-use ExercisesClient object.
    """
    client = get_private_http_client(user)
    return ExercisesClient(client)

from pydantic import BaseModel, ConfigDict, Field, UUID4


class ExerciseSchema(BaseModel):
    """
    Exercise structure
    """
    id: UUID4
    title: str
    course_id: UUID4 = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class GetExercisesQuerySchema(BaseModel):
    """
    Request structure to get an exercises list.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')


class GetExerciseResponseSchema(BaseModel):
    """
    Getting exercise response structure.
    """
    exercise: ExerciseSchema


class GetExercisesListResponseSchema(BaseModel):
    """
    Getting exercises list response structure.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
    Request structure to create exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class CreateExerciseResponseSchema(BaseModel):
    """
    Creating exercise response structure.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Request structure to update exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')


class UpdateExerciseResponseSchema(BaseModel):
    """
    Updating exercise response structure.
    """
    exercise: ExerciseSchema

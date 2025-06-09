from pydantic import BaseModel, ConfigDict, Field

from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """
    Exercise structure
    """
    id: str
    title: str
    course_id: str = Field(alias='courseId')
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

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid4)
    max_score: int = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)


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

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(BaseModel):
    """
    Updating exercise response structure.
    """
    exercise: ExerciseSchema

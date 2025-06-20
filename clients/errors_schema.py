from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ValidationErrorSchema(BaseModel):
    """
    Validation error structure
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias='ctx')
    message: str = Field(alias='msg')
    location: list[str] = Field(alias='loc')


class ValidationErrorResponseSchema(BaseModel):
    """
    Structure describing Validation error API response
    """
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias='detail')


class ClientErrorResponseSchema(BaseModel):
    """
    Structure describing client error response
    """
    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias='detail')
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserSchema(BaseModel):
    """
    User structure
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    Request structure to create user.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: str
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    """"
    Creation user response structure
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Request structure to update user.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: str | None
    lastName: str | None = Field(alias='lastName')
    firstName: str | None = Field(alias='firstName')
    middleName: str | None = Field(alias='middleName')


class UpdateUserResponseSchema(BaseModel):
    """"
    Updating user response structure
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """"
    Getting user response structure
    """
    user: UserSchema

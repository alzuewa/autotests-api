from pydantic import BaseModel, EmailStr, Field, UUID4


class UserSchema(BaseModel):
    """
    User model
    """
    id: UUID4
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    User creation request model
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    """
    User creation response model
    """
    user: UserSchema

from typing import Any

import jsonschema
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Checks if JSON-object instance conforms to provided JSON-schema
    :param instance: JSON-object instance which needs to be checked
    :param schema: expected JSON-schema
    :raises jsonschema.exceptions.ValidationError: if instance doesn't conform to schema
    """
    jsonschema.validate(instance=instance, schema=schema, format_checker=Draft202012Validator.FORMAT_CHECKER)

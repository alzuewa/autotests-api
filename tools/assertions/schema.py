from typing import Any

import allure
import jsonschema
from jsonschema.validators import Draft202012Validator

from tools.logger import get_logger

logger = get_logger('SCHEMA_ASSERTIONS')


@allure.step('Validate JSON schema')
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Checks if JSON-object instance conforms to provided JSON-schema
    :param instance: JSON-object instance which needs to be checked
    :param schema: expected JSON-schema
    :raises jsonschema.exceptions.ValidationError: if instance doesn't conform to schema
    """
    logger.info('Validate JSON schema')

    jsonschema.validate(instance=instance, schema=schema, format_checker=Draft202012Validator.FORMAT_CHECKER)

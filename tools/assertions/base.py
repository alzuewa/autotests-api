from typing import Any, Sized

import allure

from tools.logger import get_logger

logger = get_logger('BASE_ASSERTIONS')


@allure.step('Check that response status code equals {expected}')
def assert_status_code(actual: int, expected: int) -> None:
    """
    Checks that actual status code matches expected one.
    :param actual: Actual status-code
    :param expected: Expected status-code
    :return: None
    :raises: AssertionError if status-codes don't match
    """
    logger.info(f'Check that response status code equals {expected}')

    assert actual == expected, (
        'Unexpected response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}. '
    )


@allure.step('Check that {name} equals {expected}')
def assert_equal(actual: Any, expected: Any, name: str) -> None:
    """
    Checks that actual value matches expected one.
    :param actual: Actual value
    :param expected: Expected value
    :param name: Checked value name
    :return: None
    :raises: AssertionError if values don't match
    """
    logger.info(f'Check that "{name}" equals "{expected}"')

    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}. '
    )


@allure.step('Check that {name} is true')
def assert_is_true(actual: Any, name: str) -> None:
    """
    Checks that actual param has truthy value
    :param actual: Actual value
    :param name: Checked value name
    :return: None
    :raises: AssertionError if actual value isn't truthy
    """
    logger.info(f'Check that "{name}" is true')

    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected truthy value but got "{actual}" instead.'
    )


def assert_length(actual: Sized, expected: Sized, name: str) -> None:
    """
    Checks that an actual value length equals the length of expected value
    :param actual: Actual object length
    :param expected: Expected object length
    :param name: Checked object name
    :return: None
    :raises: AssertionError if objects' lengths don't match
    """
    with allure.step(f"Check that {name}'s length equals {len(expected)}"):
        logger.info(f'Check that "{name}\'s" length equals {len(expected)}')

        assert len(actual) == len(expected), (
            f'Incorrect object length: "{name}". '
            f'Expected length: {len(expected)}. '
            f'Actual length: {len(actual)}. '
        )

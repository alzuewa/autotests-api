from typing import Any

def assert_status_code(actual: int, expected: int) -> None | AssertionError:
    """
    Checks that actual status code matches expected one.
    :param actual: Actual status-code
    :param expected: Expected status-code
    :return: None
    :raises: AssertionError if status-codes don't match
    """
    assert actual == expected, (
        'Unexpected response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}. '
    )

def assert_equal(actual: Any, expected: Any, name: str) -> None | AssertionError:
    """
    Checks that actual value matches expected one.
    :param actual: Actual value
    :param expected: Expected value
    :param name: Checked value name
    :return: None
    :raises: AssertionError if values don't match
    """
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}. '
    )


from typing import Any, Sized


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


def assert_is_true(actual: Any, name: str) -> None | AssertionError:
    """
    Checks that actual param has truthy value
    :param actual: Actual value
    :param name: Checked value name
    :return: None
    :raises: AssertionError if actual value isn't truthy
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected truthy value but got "{actual}" instead.'
    )


def assert_length(actual: Sized, expected: Sized, name: str) -> None | AssertionError:
    """
    Checks that an actual value length equals the length of expected value
    :param actual: Actual object length
    :param expected: Expected object length
    :param name: Checked object name
    :return: None
    :raises: AssertionError if objects' lengths don't match
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length: "{name}". '
        f'Expected length: {len(expected)}. '
        f'Actual length: {len(actual)}. '
    )

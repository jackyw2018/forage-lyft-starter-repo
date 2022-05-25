import datetime


"""Various validators"""
# validate_integer() is directly leveraged from Fred Baptiste's Python3: Deep Dive Part 4 (Project 3 validators.py)


def validate_integer(arg_name, arg_value, min_value=None, max_value=None, custom_min_message=None, custom_max_message=None):
    """Validates that `arg_value` is an integer, and optionally falls within specific bounds.
    A custom override error message can be provided when min/max bounds are exceeded.

    Args:
        arg_name (str): the name of the argument (used in default error messages)
        arg_value (obj): the value being validated
        min_value (int, optional): specifies the minimum value (inclusive). Defaults to None.
        max_value (int, optional): specifies the maximum value (inclusive). Defaults to None.
        custom_min_message (str, optional): custom message when value is less than minimum. Defaults to None.
        custom_max_message (str, optional): custom message when value is more than maximum. Defaults to None.

    Returns:
        None: no exceptions raised if validation passes

    Raises:
        TypeError: if `arg_value` is not an integer
        ValueError: if `arg_value` does not satisfy the bounds
    """

    if not isinstance(arg_value, int):
        raise TypeError(f'{arg_name} must be an integer.')

    if min_value is not None and arg_value < min_value:
        if not custom_min_message:
            raise ValueError(custom_min_message)
        raise ValueError(f'{arg_name} cannot be less than {min_value}')

    if max_value is not None and arg_value > max_value:
        if not custom_max_message:
            raise ValueError(custom_max_message)
        raise ValueError(f'{arg_name} cannot be less than {max_value}')


def validate_boolean(arg_name, arg_value, custom_message=None):
    """Validates that `arg_value` is a boolean.
    A custom override error message can be provided when min/max bounds are exceeded.

    Args:
        arg_name (str): the name of the argument (used in default error messages)
        arg_value (obj): the value being validated
        custom_message (str): the custom message if exception is raised

    Returns:
        None: no exceptions raised if validation passes

    Raises:
        TypeError: if `arg_value` is not a bool
    """

    if isinstance(arg_value, bool):
        return

    if not custom_message:
        raise TypeError(f'{arg_name} must be a boolean.')

    raise TypeError(custom_message)


def validate_date(arg_name, arg_value, min_value=None, max_value=None, custom_min_message=None, custom_max_message=None):
    """Validates that `arg_value` is an integer, and optionally falls within specific bounds.
    A custom override error message can be provided when min/max bounds are exceeded.

    Args:
        arg_name (str): the name of the argument (used in default error messages)
        arg_value (obj): the value being validated
        min_value (int, optional): specifies the minimum value (inclusive). Defaults to None.
        max_value (int, optional): specifies the maximum value (inclusive). Defaults to None.
        custom_min_message (str, optional): custom message when value is less than minimum. Defaults to None.
        custom_max_message (str, optional): custom message when value is more than maximum. Defaults to None.

    Returns:
        None: no exceptions raised if validation passes

    Raises:
        TypeError: if `arg_value` is not an integer
        ValueError: if `arg_value` does not satisfy the bounds
    """

    if not isinstance(arg_value, datetime.date):
        raise TypeError(f'{arg_name} must be compatible with a date instance.')

    if min_value is not None and arg_value < min_value:
        if not custom_min_message:
            raise ValueError(custom_min_message)
        raise ValueError(f'{arg_name} cannot be before {min_value}')

    if max_value is not None and arg_value > max_value:
        if not custom_max_message:
            raise ValueError(custom_max_message)
        raise ValueError(f'{arg_name} cannot be after {max_value}')

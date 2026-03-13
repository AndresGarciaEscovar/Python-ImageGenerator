"""
    Contains the functions for general validation of general lattice
    properties.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# General
from typing import Any, Union


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _validate_list_parameters(length: Any, exception: Any) -> None:
    """
        Validates the parameters passed to the 'validate_list' function.

        :param length: The length of the list to validate. Must be an integer
         value.

        :param texecpt: A boolean flag. Must be True or False.

        :raise: TypeError: If the parameters are not of the expected type.
    """
    # Auxiliary variables.
    string: str = "\"validate_list\""

    # Validate the length.
    if not isinstance(length, int):
        raise TypeError(
            f"The \"length\" parameter of the {string} function must be "
            f"an integer. Current type: {type(length).__name__}."
        )

    # Validate the exception parameter.
    if not isinstance(exception, bool):
        raise TypeError(
            f"The \"exception\" parameter of the {string} function must be "
            f"a boolean. Current type: {type(exception).__name__}."
        )


def _validate_real_parameters(zero: Any, exception: Any) -> None:
    """
        Validates the parameters passed to the 'validate_real' function.

        :param zero: A boolean flag. Must be True or False.

        :param exception: A boolean flag. Must be True or False.

        :raise: TypeError: If the parameters are not of the expected type.
    """
    # Auxiliary variables.
    string: str = "\"validate_real\""

    # Validate the zero parameter.
    if not isinstance(zero, bool):
        raise TypeError(
            f"The \"zero\" parameter of the {string} function must be "
            f"a boolean. Current type: {type(zero).__name__}."
        )

    # Validate the exception parameter.
    if not isinstance(exception, bool):
        raise TypeError(
            f"The \"exception\" parameter of the {string} function must be "
            f"a boolean. Current type: {type(exception).__name__}."
        )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate_bool(
    value: Any,
    name: Union[None, str] = None,
    exception: bool = False
) -> bool:
    """
        Function that validates that the value is a boolean quantity.
        Raises an exception if validation fails and exception is True.

        :param value: The value to validate.

        :param name: The name of the variable.

        :param exception: A boolean flag that indicates if an exception should
         be raised if the object is not the expected type. True, if an
         exception must be raised; False, otherwise. False, by default.

        :return: True, if the object is a boolean variable; False,
         otherwise.

        :raises TypeError: If the object is not a real positive number and
         exception is True.
    """
    # Auxiliary variables.
    flag: bool = isinstance(value, bool)

    # Raise an exception if needed.
    if not flag and exception:
        error: str = ' ' if name is None else f' \"{name}\" '

        raise TypeError(
            f"The value{error}is not a boolean variable; current type: "
            f"{type(value).__name__}."
        )

    return flag


def validate_list(
    value: Any,
    dtype: Any,
    length: int = -1,
    name: Union[None, str] = None,
    exception: bool = False
) -> bool:
    """
        Function that validates that the type of the object is the expected
        type. Raises an exception if validation fails and exception is True.

        :param value: The value to validate.

        :param dtype: The expected type of the value.

        :param length: The length of the list to validate. Must be an integer
         value. -1, by default.

        :param name: The name of the variable.

        :param exception: A boolean flag that indicates if an exception should
         be raised if the object is not the expected type. True, if an
         exception must be raised; False, otherwise. False, by default.

        :return: True, if the object is of the specified type; False,
         otherwise.

        :raises TypeError: If the object is not of the specified type and
         exception is True.
    """
    # Auxiliary variables.
    message: str = ""

    # Validate the mandatory parameters.
    _validate_list_parameters(length, exception)

    # Check the different properties.
    if not isinstance(value, list):
        message += "The value is not a list."

    elif len(value) > 0 and not all(isinstance(x, dtype) for x in value):
        message += (
            f"The list's elements are all not {dtype}s. Types: "
            f"{tuple(type(x) for x in value)}."
        )

    elif length > -1 and len(value) != length:
        message += f"The list's length is not {length}."

    # Raise an exception if needed.
    flag: bool = message == ""

    if not flag and exception:
        error: str = " " if name is None else f" \"{name}\" "

        raise TypeError(f"The list{error}is not valid. {message}".strip())

    return flag


def validate_positive_int(
    value: Any,
    zero: bool = True,
    name: Union[None, str] = None,
    exception: bool = False
) -> bool:
    """
        Function that validates that the value is an integer positive number.
        Raises an exception if validation fails and exception is True.

        :param value: The value to validate.

        :param zero: The value can be zero. True, if the value can be zero;
         False, otherwise. True, by default.

        :param name: The name of the variable.

        :param exception: A boolean flag that indicates if an exception should
         be raised if the object is not the expected type. True, if an
         exception must be raised; False, otherwise. False, by default.

        :return: True, if the object is an integer positive number; False,
         otherwise.

        :raises TypeError: If the object is not an integer positive number and
         exception is True.
    """
    # Auxiliary variables.
    message: str = ""

    # Validate the parameters.
    _validate_real_parameters(zero, exception)

    # Check that the value is positive.
    if not isinstance(value, int):
        message += "The value is not an integer number."

    elif not (value >= 0 if zero else value > 0):
        message += "The integer value is not positive."

    # Raise an exception if needed.
    flag: bool = message == ""

    if not flag and exception:
        error: str = " " if name is None else f" \"{name}\" "

        raise TypeError(
            f"The value{error}is not an integer positive number. Current "
            f"value: {value}. {message}".strip()
        )

    return flag


def validate_positive_real(
    value: Any,
    zero: bool = True,
    name: Union[None, str] = None,
    exception: bool = False
) -> bool:
    """
        Function that validates that the value is a real positive number.
        Raises an exception if validation fails and exception is True.

        :param value: The value to validate.

        :param zero: The value can be zero. True, if the value can be zero;
         False, otherwise. True, by default.

        :param name: The name of the variable.

        :param exception: A boolean flag that indicates if an exception should
         be raised if the object is not the expected type. True, if an
         exception must be raised; False, otherwise. False, by default.

        :return: True, if the object is a real positive number; False,
         otherwise.

        :raises TypeError: If the object is not a real positive number and
         exception is True.
    """
    # Auxiliary variables.
    message: str = ""

    # Validate the parameters.
    _validate_real_parameters(zero, exception)

    # Check the different properties.
    if not isinstance(value, (int, float)):
        message += "The value is not a real number."

    elif not (value >= 0 if zero else value > 0):
        message += "The value is not positive."

    # Raise an exception if required.
    flag: bool = message == ""

    if not flag and exception:
        error: str = " " if name is None else f" \"{name}\" "

        raise TypeError(
            f"The value{error}is not a real positive number. Current value: "
            f"{value}. {message}".strip()
        )

    return flag

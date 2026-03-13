"""
    File that contains the functions for the validation of different
    quantities.
"""

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# General
from typing import Any


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate_type(value: Any, dtype: Any, exception: bool = True) -> bool:
    """
        Function that validates that the type of the object is the expected
        type.

        :param value: The value to validate.

        :param dtype: The expected type of the value.

        :param exception: A boolean flag that indicates if an exception should
         be raised if the object is not the expected type. True, if an
         exception should be raised; False, otherwise. True, by default.

        :return: True, if the object is of the specified type; False,
         otherwise.

        :raises TypeError: If the object is not of the specified type and
         exception is True.
    """
    # Check that the object is the given type.
    flag: bool = isinstance(value, dtype)

    if not flag and exception:
        raise TypeError(
            f"The value's type is not a {dtype}. Current type: "
            f"{type(value).__name__}."
        )

    return flag


def validate_type_negative(
    value: Any,
    dtype: Any,
    zero: bool = False,
    exception: bool = True
) -> bool:
    """
        Function that validates that the type of the object is the expected
        type and that the value is negative. If the zero option is set to True,
        then the value can be zero.

        :param value: The value to validate.

        :param dtype: The expected type of the value.

        :param zero: A boolean flag that indicates if the value can be zero.
         True, if the value can be zero; False, otherwise. False, by default.

        :param exception: A boolean flag that indicates if an exception should
         be raised if the object is not of the expected type and negative.
         True, if an exception should be raised; False, otherwise. True, by
         default.

        :return: True, if the object is a negative number of the specified
         type; False, otherwise.

        :raises ValueError: If the object is not a negative number or zero, the
         latter if the zero option is set to True, and exception is True.
    """
    # Auxiliary variables.
    flag: bool = validate_type(value, dtype, exception)
    flag = flag and (value <= 0 if zero else value < 0)

    if not flag and exception:
        raise ValueError(
            f"The value is not a negative number{' or zero' if zero else ''}; "
            f"current value: {value}."
        )

    return flag


def validate_type_positive(
    value: Any,
    dtype: Any,
    zero: bool = False,
    exception: bool = True
) -> bool:
    """
        Function that validates that the type of the object is the expected
        type and that the value is positive. If the zero option is set to True,
        then the value can be zero.

        :param value: The value to validate.

        :param dtype: The expected type of the value.

        :param zero: A boolean flag that indicates if the value can be zero.
         True, if the value can be zero; False, otherwise. False, by default.

        :param exception: A boolean flag that indicates if an exception should
         be raised if the object is not of the expected type and positive.
         True, if an exception should be raised; False, otherwise. True, by
         default.

        :return: True, if the object is a positive number of the specified
         type; False, otherwise.

        :raises ValueError: If the object is not a positive number or zero, the
         latter if the zero option is set to True, and exception is True.
    """
    # Auxiliary variables.
    flag: bool = validate_type(value, dtype, exception)
    flag =  flag and (value >= 0 if zero else value > 0)

    if not flag and exception:
        raise ValueError(
            f"The value is not a positive number{' or zero' if zero else ''}; "
            f" current value: {value}."
        )

    return flag

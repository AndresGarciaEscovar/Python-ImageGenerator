"""
    File that contains the functions for the validation of different quantities.
"""

# ##############################################################################
# Imports
# ##############################################################################


# General
from typing import Any


# ##############################################################################
# Global Variables
# ##############################################################################


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate_type(value: Any, dtype: Any, texcept: bool = True) -> bool:
    """
        Function that validates that the type of the object is the expected
        type.

        :param value: The value to validate.

        :param dtype: The expected type of the value.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not the expected type. True, if an exception
         should be raised; False, otherwise. True, by default.

        :return: True, if the object is of the specified type; False,
         otherwise.

        :raises TypeError: If the object is not of the specified type and
         texcept is True.
    """
    # Check that the object is the given type.
    flag = isinstance(value, dtype)
    if not flag and texcept:
        raise TypeError(
            f"The value's type is not a {dtype}. Current type: {type(value)}."
        )

    return flag


def validate_type_negative(
    value: Any, dtype: Any, zero: bool = False, texcept: bool = True
) -> bool:
    """
        Function that validates that the type of the object is the expected
        type and that the value is negative. If the zero option is set to True,
        then the value can be zero.

        :param value: The value to validate.

        :param dtype: The expected type of the value.

        :param zero: A boolean flag that indicates if the value can be zero.
         True, if the value can be zero; False, otherwise. False, by default.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not of the expected type and negative. True, if
         an exception should be raised; False, otherwise. True, by default.

        :return: True, if the object is a negative number of the specified type;
         False, otherwise.

        :raises ValueError: If the object is not a negative number or zero, the
         latter if the zero option is set to True, and texcept is True.
    """
    # Check that the object is the given type.
    if not (flag := validate_type(value, dtype, texcept)):
        return False

    # Check that the value is negative.
    flag = flag and (value <= 0 if zero else value < 0)
    if not flag and texcept:
        # Format the option.
        zero_opt = " or zero" if zero else ""

        raise ValueError(
            f"The value is not a negative number{zero_opt}. Current value: "
            f"{value}."
        )

    return flag


def validate_type_positive(
    value: Any, dtype: Any, zero: bool = False, texcept: bool = True
) -> bool:
    """
        Function that validates that the type of the object is the expected
        type and that the value is positive. If the zero option is set to True,
        then the value can be zero.

        :param value: The value to validate.

        :param dtype: The expected type of the value.

        :param zero: A boolean flag that indicates if the value can be zero.
         True, if the value can be zero; False, otherwise. False, by default.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not of the expected type and positive. True, if
         an exception should be raised; False, otherwise. True, by default.

        :return: True, if the object is a positive number of the specified type;
         False, otherwise.

        :raises ValueError: If the object is not a positive number or zero, the
         latter if the zero option is set to True, and texcept is True.
    """
    # Check that the object is the given type.
    if not (flag := validate_type(value, dtype, texcept)):
        return False

    # Check that the value is positive.
    flag = flag and (value >= 0 if zero else value > 0)
    if not flag and texcept:
        # Format the option.
        zero_opt = " or zero" if zero else ""

        raise ValueError(
            f"The value is not a positive number{zero_opt}. Current value: "
            f"{value}."
        )

    return flag

"""
    Contains the functions for general validation of general lattice properties.
"""


# ##############################################################################
# Imports
# ##############################################################################


# General
from typing import Any


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate_list_parameters(length: Any, texcept: Any) -> None:
    """
        Validates the parameters passed to the 'validate_list' function.

        :param length: The length of the list to validate. Must be an integer
         value.

        :param texecpt: A boolean flag. Must be True or False.

        :raise: TypeError: If the parameters are not of the expected type.
    """
    # Auxiliary variables.
    fstring = "\"validate_list\""

    # Validate the length.
    if not isinstance(length, int):
        raise TypeError(
            f"The \"length\" parameter of the {fstring} function must be "
            f"an integer. Current type: {type(length)}."
        )

    # Validate the texcept parameter.
    if not isinstance(texcept, bool):
        raise TypeError(
            f"The \"texcept\" parameter of the {fstring} function must be "
            f"a boolean. Current type: {type(texcept)}."
        )


def _validate_real_parameters(zero: Any, texcept: Any) -> None:
    """
        Validates the parameters passed to the 'validate_real' function.

        :param zero: A boolean flag. Must be True or False.

        :param texcept: A boolean flag. Must be True or False.

        :raise: TypeError: If the parameters are not of the expected type.
    """
    # Auxiliary variables.
    fstring = "\"validate_real\""

    # Validate the zero parameter.
    if not isinstance(zero, bool):
        raise TypeError(
            f"The \"zero\" parameter of the {fstring} function must be "
            f"a boolean. Current type: {type(zero)}."
        )

    # Validate the texcept parameter.
    if not isinstance(texcept, bool):
        raise TypeError(
            f"The \"texcept\" parameter of the {fstring} function must be "
            f"a boolean. Current type: {type(texcept)}."
        )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate_list(
    value: Any, dtype: Any, length: int = -1, name: str = None,
    texcept: bool = False
) -> bool:
    """
        Function that validates that the type of the object is the expected
        type. Raises an exception if validation fails and texcept is True.

        :param value: The value to validate.

        :param dtype: The expected type of the value.

        :param length: The length of the list to validate. Must be an integer
         value. -1, by default.

        :param name: The name of the variable.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not the expected type. True, if an exception
         should be raised; False, otherwise. False, by default.

        :return: True, if the object is of the specified type; False,
         otherwise.

        :raises TypeError: If the object is not of the specified type and
         texcept is True.
    """
    # Validate the mandatory parameters.
    _validate_list_parameters(length, texcept)

    # Validate the other parameters.
    flag = (flag0 := isinstance(value, list))
    message = "" if flag else "The value is not a list. "

    # Check the list's elements' types.
    if flag0 and len(value) > 0:
        dtypes = tuple(isinstance(x, dtype) for x in value)
        flag = (flag1 := all(dtypes)) and flag
        message += "" if flag1 else (
            f"The list's elements are all not {dtype}s. Types: "
            f"{tuple(type(x) for x in value)}. "
        )

    # Check the list's length.
    if flag0 and length > -1:
        flag = (flag1 := len(value) == length) and flag
        message += "" if flag1 else f"The list's length is not {length}. "

    # Raise an exception if required.
    if texcept and not flag:
        tname = " " if name is None else f" \"{name}\" "
        raise TypeError(f"The list{tname}is not valid. {message}".strip())

    return flag


def validate_real_positve(
    value: Any, zero: bool = True, name: str = None,  texcept: bool = False
) -> bool:
    """
        Function that validates that the value is a real positive number.
        Raises an exception if validation fails and texcept is True.

        :param value: The value to validate.

        :param zero: The value can be zero. True, if the value can be zero;
         False, otherwise. True, by default.

        :param name: The name of the variable.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not the expected type. True, if an exception
         should be raised; False, otherwise. False, by default.

        :return: True, if the object is a real positive number; False,
         otherwise.

        :raises TypeError: If the object is not a real positive number and
         texcept is True.
    """
    # Validate the parameters.
    _validate_real_parameters(zero, texcept)

    # Validate the value.
    flag = isinstance(value, (int, float))
    message = "" if flag else "The value is not a real number. "

    # Check that the value is positive.
    if flag:
        flag = value >= 0 if zero else value > 0
        message += "" if flag else f"The value is not positive. "

    # Raise an exception if required.
    if texcept and not flag:
        tname = " " if name is None else f" \"{name}\" "
        raise TypeError(
            f"The value{tname}is not a real positive number. Current value: "
            f"{value}. {message}".strip()
        )

    return flag

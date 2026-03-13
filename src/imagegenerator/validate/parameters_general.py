"""
    Contains the code to validate the general parameters of the code.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _validate_combination(positional: list, display: bool) -> None:
    """
        Validates the parameter combination is valid.

        :param positional: The list of positional parameters, where both must
         be strings.

        :param display: The boolean flag indicating whether the requested
         configuration must be printed to the screen. True, if the
         configuration must be printed to the screen; False, otherwise.

        :raise ValueError: If the combination of parameters is not valid.
    """
    # Validate the type is correct.
    if len(positional) > 1 and display:
        raise ValueError(
            "If the display flag is being used, there must only be a single "
            "positional argument; there are currently two arguments."
        )


def _validate_display(display: Any) -> None:
    """
        Validates the parameter passed is a boolean flag.

        :param display: The object to verify.

        :raise TypeError: If the "display" parameter is not a boolean value.
    """
    # Validate the type is correct.
    if isinstance(display, bool):
        raise TypeError(
            f"The \"display\" argument is not a boolean value; current type: "
            f"{type(display).__name__}."
        )


def _validate_positional(positional: Any) -> None:
    """
        Validates the parameters passed, must be a list of strings, with at
        the most 2 entries.

        :param positional: The object to verify.

        :raise TypeError: If the "position" parameter is not a list.

        :raise ValueError: If the "position" list does not have at least one
         element and at most two. If the items in the "position" list are NOT
         strings.
    """
    # Auxiliary variables.
    flag: bool = isinstance(positional, list)
    maximum: int = 3
    message: str = ""

    # Validate the type is correct.
    if not flag:
        raise TypeError(
            f"The \"positional\" arguments is not a list; current type: "
            f"{type(positional).__name__}."
        )

    # Validate that the values are correct.
    if len(positional) not in range(1, maximum):
        message += (
            f"The list must contain at least one item, but no more than two; "
            f"current length is: {len(positional)}. "
        )

    if not all(isinstance(x, str) for x in positional):
        message += (
            "Not all the arguments in the positional arguments are strings; "
            "they must all be strings. "
        )

    if message != "":
        raise ValueError(message.strip())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate(positional: Any, display: Any) -> None:
    """
        Validates the parameters passed.

        :param positional: The list with the organized positional parameters.

        :param display: A boolean flag indicating whether the default
         parameters must be printed.
    """
    # Validate the parameters: One at a time.
    _validate_display(display)
    _validate_positional(positional)

    # In combination.
    _validate_combination(positional, display)

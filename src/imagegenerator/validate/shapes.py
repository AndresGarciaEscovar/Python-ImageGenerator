"""
    Contains the functions to validate the different parameters passed to the
    functions.
"""

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate_coordinate(coordinate: tuple) -> None:
    """
        Validates that the given coordinate is a real number, i.e., an integer
        or a floating point number.

        :param coordinate: A collection of numbers that represent an
         N-dimensional coordinate.

        :raise TypeError: If the coordinates are not real numbers, and the
         coordinate itself is NOT a tuple.
    """
    # Must be a tuple.
    if not (isinstance(coordinate, tuple) and len(coordinate) == 2):
        flag: bool = isinstance(coordinate, tuple)
        msg: str = "" if not flag else f"; current length {len(coordinate)}"

        raise TypeError(
            f"The coordinate must be a 2-tuple of real numbers; current type "
            f"{type(coordinate).__name__}{msg}."
        )

    # A tuple of real number.
    if not all(isinstance(x, (float, int)) for x in coordinate):
        raise TypeError(
            "There are variables in the coordinate that are not real numbers; "
            "make sure to only give real numbers."
        )


def validate_tick

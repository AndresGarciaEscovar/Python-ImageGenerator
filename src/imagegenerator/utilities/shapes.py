"""
    File that contains the functions to generate the different shapes.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _validate_coordinate(coordinate: tuple) -> None:
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


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def get_coordinate(coordinate: tuple) -> str:
    """
        From the given coordinate, gets the string representation of the value.

        :param coordinate: The coordinate to be converted into a string.

        :return: A string representing the coordinate.
    """
    # Validate the coordinate.
    _validate_coordinate(coordinate)

    return f"({', '.join(f'{float(x):+.4f}' for x in coordinate)})"


# #############################################################################
# TO DELETE
# #############################################################################


def run() -> None:
    """
        Runs the main code.
    """
    numbers: tuple = 9, 0
    coordinate: str = get_coordinate(numbers)

    print(coordinate)


# -----------------------------------------------------------------------------
# Main Program
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    run()

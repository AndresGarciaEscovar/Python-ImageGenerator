"""
    File that contains the functions to generate the different shapes.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Callable

# User.
import imagegenerator.validate.shapes as vshapes


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def get_coordinate(coordinate: tuple, units: str = "cm") -> str:
    """
        From the given coordinate, gets the string representation of the value.

        :param coordinate: The coordinate to be converted into a string.

        :return: A string representing the coordinate.
    """
    # Validate the coordinate.
    vshapes.validate_coordinate(coordinate)

    return f"({', '.join(f'{float(x):+.4f}{units}' for x in coordinate)})"


def get_tick(
    base: float = 0.5,
    vertical: float = 1.0,
    position: tuple = (0, 0),
    offset: tuple = (0, 0),
    units: str = "cm"
) -> str:
    """
        Gets the code for a tick.

        :param base: The base of the tick; must be a positive real number
         greater than zero.

        :param vertical: The length of the vertical part of the tick.

        :param position: A tuple that represents the position of the middle of
         point of the base along the base.

        :param offset: The horizontal and vertical offset of the lower part of
         the tick with respect to the horizontal middle of the base (along the
         x-axis), and above the base (along the y-axis). Negative numbers
         represent left/right and top/bottom.

        :return: A string with the TikZ code for a simple tick.
    """
    # Auxiliary variables.
    function: Callable = lambda x: get_coordinate(x, units)

    # Get the coordinates.
    positions_base: tuple = (
        (-base / 2.0 + position[0], position[1]),
        (+base / 2.0 + position[0], position[1]),
    )
    positions_vertical: tuple = (
        (position[0] + offset[0], position[1] + offset[1]),
        (position[0] + offset[0], position[1] + offset[1] + vertical),
    )

    positions_base = tuple(function(x) for x in positions_base)
    positions_vertical = tuple(function(x) for x in positions_vertical)

    return (
        f"\\draw {' -- '.join(positions_base)};\n"
        f"\\draw {' -- '.join(positions_vertical)};"
    )


# #############################################################################
# TO DELETE
# #############################################################################


def run() -> None:
    """
        Runs the main code.
    """
    print(get_tick())


# -----------------------------------------------------------------------------
# Main Program
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    run()

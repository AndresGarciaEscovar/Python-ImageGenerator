"""
    Functions to run the main program.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from argparse import ArgumentParser, Namespace


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Programs.
PROGRAM: str = "Stochastic Model - Image Generator"
DESCRIPTION: str = """
Program to generate images for the lattices of different stochastic models. It
can be used to present schematics of different possible models.
""".strip()
USAGE: str = """
imagegenerator <name of model> <optional: path to config. file> [-p]
""".strip()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_arguments() -> dict:
    """
        Gets the parameters to generate the lattice.

        :return: A dictionary with the parameters of the lattice related to
         the physical model.
    """
    # Create the parser.
    parser: ArgumentParser = ArgumentParser(
        description=DESCRIPTION,
        prog=PROGRAM,
        usage=USAGE
    )

    # Define the arguments: positional.
    parser.add_argument(
        "arguments",
        nargs="+",
        type=str,
        help=(
            "Program arguments, at least the name of the model must be "
            "provided."
        )
    )

    # Define the arguments: optional.
    parser.add_argument(
        "-p",
        "--print",
        action="store_true",
        help=(
            "Boolean flag indicating whether the list of possible arguments "
            "for the model must be printed."
        )
    )

    # Read the arguments.
    args: Namespace =  parser.parse_args()

    return {
        "arguments": args.arguments,
        "print": args.print
    }


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def main() -> None:
    """
        Runs the main program.
    """
    # Read the arguments.
    arguments: dict = _get_arguments()

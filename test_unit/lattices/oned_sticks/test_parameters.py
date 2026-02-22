"""
    File that contains the unit test for the functions in the file
    validate_general_1d.py.
"""

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# General
import copy as cp
import pathlib
import unittest
import yaml

# User defined
import latexlattices.lattices.oned_sticks.parameters as parameters


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestParameters(unittest.TestCase):
    """
        Class that contains the tests for the validation of the 1D Sticks
        lattice parameters.
    """

    def test_get(self):
        """
            Test the function get the dictionary. The test gets the dictionary
            and must validate all the parameters and NOT throw an expection.
        """
        # Gets the parameters.
        configuration = parameters.get()
        parameters.validate(configuration)

    def test_validate(self):
        """
            Test the function get the dictionary. The test gets the dictionary
            and must validate all the parameters.
        """
        name = "test_parameters.yaml"
        path = pathlib.Path(__file__).parent.absolute() / name

        with open(f"{path}", encoding="utf-8", mode="w") as fl:
            configuration = yaml.safe_load(fl)

        valid = configuration["valid"]
        invalid = configuration["invalid"]

        del configuration

        # ---------------------------------------------------------------------
        # Test 0: Valid parameters must not throw an exception.
        # ---------------------------------------------------------------------

        # Check the valid parameters.
        parameters.validate(valid)

        # ---------------------------------------------------------------------
        # Test 1: Invalid parameters must throw an exception.
        # ---------------------------------------------------------------------

        # Check every invalid parameter.
        for key in valid.keys():
            for subkey in valid[key].keys():
                values = invalid[key][subkey]

                # Set the invalid parameters, one at a time.
                for value in values:
                    testinvalid = cp.deepcopy(valid)
                    testinvalid[key][subkey] = value

                    # Must get an exception.
                    expected = (TypeError, ValueError)
                    message = (
                        f"A TypeError or ValueError must be thrown; thrown by "
                        f"\"{key}.{subkey}\": {value}"
                    )

                    with self.assertRaises(expected, msg=message):
                        parameters.validate(testinvalid)

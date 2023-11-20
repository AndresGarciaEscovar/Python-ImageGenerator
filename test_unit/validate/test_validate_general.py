"""
    File that contains the unit test for the functions in the file
    validate_general_1d.py.
"""


# ##############################################################################
# Imports
# ##############################################################################


# General
import numpy as np
import unittest

# User defined
import latexlattices.validate.validate_general as vgeneral


# ##############################################################################
# Classes
# ##############################################################################


class TestValidateGeneral(unittest.TestCase):
    """
        Class that contains the tests for the validation of several non lattice
        quantities.
    """

    def test_validate_type(self):
        """
            Test the function validate_type.
        """
        # Auxiliary variables.
        ntypes = (list, tuple, set, np.ndarray, int, float, complex)
        values = list(x for x in range(3))

        for dtype in ntypes:
            # ------------------------------------------------------------------
            # Test 1: The input is of the specified type.
            # ------------------------------------------------------------------
            value = dtype(values) if dtype in ntypes[:4] else dtype(1)
            self.assertTrue(vgeneral.validate_type(value, dtype))

            # ------------------------------------------------------------------
            # Test 2: The input is of a different type.
            # ------------------------------------------------------------------

            # Change the type of the array.
            tdtype = [x for x in ntypes if x != dtype][0]
            value = tdtype(values) if tdtype in ntypes[:3] else tdtype(1)

            # Test for different types.
            self.assertFalse(
                vgeneral.validate_type(value, dtype, texcept=False)
            )

            # An exception should be raised.
            with self.assertRaises(TypeError):
                vgeneral.validate_type(value, dtype, texcept=True)

    def test_validate_type_negative(self):
        """
            Test the function validate_type_negative.
        """
        # Auxiliary variables.
        ntypes = (int, float)

        for dtype in ntypes:
            # ------------------------------------------------------------------
            # Test 1: The input is a negative value.
            # ------------------------------------------------------------------

            # Value is positive.
            value = -dtype(1)
            self.assertTrue(vgeneral.validate_type_negative(value, dtype))

            # Value is zero.
            value = dtype(0)

            self.assertFalse(
                vgeneral.validate_type_negative(value, dtype, texcept=False)
            )
            self.assertTrue(
                vgeneral.validate_type_negative(value, dtype, zero=True)
            )

            with self.assertRaises(ValueError):
                self.assertTrue(vgeneral.validate_type_negative(value, dtype))

            # ------------------------------------------------------------------
            # Test 2: The input is a positve value.
            # ------------------------------------------------------------------

            # Value is negative.
            value = dtype(1)

            self.assertFalse(
                vgeneral.validate_type_negative(value, dtype, texcept=False)
            )

            with self.assertRaises(ValueError):
                self.assertTrue(vgeneral.validate_type_negative(value, dtype))

    def test_validate_type_positive(self):
        """
            Test the function validate_type_positive.
        """
        # Auxiliary variables.
        ntypes = (int, float)

        for dtype in ntypes:
            # ------------------------------------------------------------------
            # Test 1: The input is a positive value.
            # ------------------------------------------------------------------

            # Value is positive.
            value = dtype(1)
            self.assertTrue(vgeneral.validate_type_positive(value, dtype))

            # Value is zero.
            value = dtype(0)

            self.assertFalse(
                vgeneral.validate_type_positive(value, dtype, texcept=False)
            )
            self.assertTrue(
                vgeneral.validate_type_positive(value, dtype, zero=True)
            )

            with self.assertRaises(ValueError):
                self.assertTrue(vgeneral.validate_type_positive(value, dtype))

            # ------------------------------------------------------------------
            # Test 2: The input is a negative value.
            # ------------------------------------------------------------------

            # Value is negative.
            value = -dtype(1)

            self.assertFalse(
                vgeneral.validate_type_positive(value, dtype, texcept=False)
            )

            with self.assertRaises(ValueError):
                self.assertTrue(vgeneral.validate_type_positive(value, dtype))

r'''
Date: 2022-05-28 17:01:33
LastEditors: Kunyang Xie
LastEditTime: 2022-05-29 17:36:15
'''
import unittest

from .token_with_escape import token_with_escape
from .token_with_escape_mutant1 import token_with_escape_mutant1
from .token_with_escape_mutant2 import token_with_escape_mutant2


class CoverageTests(unittest.TestCase):
    def test_statement_coverage(self):
        """Add tests to achieve statement coverage (as many as needed)."""
        # YOUR CODE HERE
        self.assertEqual(token_with_escape("He^llo|world"), ["Hello", "world"])

    def test_kill_mutant_1(self):
        """Kill mutant 1"""
        # YOUR CODE HERE
        self.assertEqual(token_with_escape_mutant1(
            "He^llo|world"), ["Hello", "world"])

    def test_kill_mutant_2(self):
        """Kill mutant 2"""
        # YOUR CODE HERE
        self.assertEqual(token_with_escape_mutant2(
            "He^llo|world"), ["Hello", "world"])

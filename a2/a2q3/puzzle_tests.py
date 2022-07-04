r'''
Date: 2022-05-05 14:52:01
LastEditors: Kunyang Xie
LastEditTime: 2022-07-04 18:22:41
'''
import unittest

from .magic_square import solve_magic_square


class PuzzleTests (unittest.TestCase):

    def setUp(self):
        """Reset Z3 context between tests"""
        import z3
        z3._main_ctx = None

    def tearDown(self):
        """Reset Z3 context after test"""
        import z3
        z3._main_ctx = None

    def test_1(self):
        res = solve_magic_square(3, 1, 1, 5)
        # since the solution may not be unique, the best way to test
        # is to check the all the sums
        self.assertEquals(sum([res[0][j] for j in range(3)]), 15)
        self.assertEquals(sum([res[1][j] for j in range(3)]), 15)
        self.assertEquals(sum([res[2][j] for j in range(3)]), 15)
        self.assertEquals(sum([res[i][0] for i in range(3)]), 15)
        self.assertEquals(sum([res[i][1] for i in range(3)]), 15)
        self.assertEquals(sum([res[i][2] for i in range(3)]), 15)
        self.assertEquals(sum([res[i][i] for i in range(3)]), 15)
        self.assertEquals(sum([res[i][3 - i - 1] for i in range(3)]), 15)

    def test_2(self):
        res = solve_magic_square(3, 0, 1, 9)
        # since the solution may not be unique, the best way to test
        # is to check the all the sums
        self.assertEquals(sum([res[0][j] for j in range(3)]), 15)
        self.assertEquals(sum([res[1][j] for j in range(3)]), 15)
        self.assertEquals(sum([res[2][j] for j in range(3)]), 15)
        self.assertEquals(sum([res[i][0] for i in range(3)]), 15)
        self.assertEquals(sum([res[i][1] for i in range(3)]), 15)
        self.assertEquals(sum([res[i][2] for i in range(3)]), 15)
        self.assertEquals(sum([res[i][i] for i in range(3)]), 15)
        self.assertEquals(sum([res[i][3 - i - 1] for i in range(3)]), 15)

    def test_3(self):
        res = solve_magic_square(4, 2, 2, 8)
        # since the solution may not be unique, the best way to test
        # is to check the all the sums
        self.assertEquals(sum([res[0][j] for j in range(4)]), 34)
        self.assertEquals(sum([res[1][j] for j in range(4)]), 34)
        self.assertEquals(sum([res[2][j] for j in range(4)]), 34)
        self.assertEquals(sum([res[i][0] for i in range(4)]), 34)
        self.assertEquals(sum([res[i][1] for i in range(4)]), 34)
        self.assertEquals(sum([res[i][2] for i in range(4)]), 34)
        self.assertEquals(sum([res[i][i] for i in range(4)]), 34)
        self.assertEquals(sum([res[i][4 - i - 1] for i in range(4)]), 34)

    def test_4(self):
        res = solve_magic_square(3, 1, 1, 0)
        self.assertEquals(res, None)

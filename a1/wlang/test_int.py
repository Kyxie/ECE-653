r'''
Date: 2022-05-05 14:52:01
LastEditors: Kunyang Xie
LastEditTime: 2022-06-03 16:04:32
'''
# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import unittest

from . import ast, int


class Visitor(ast.AstVisitor):
    def __init__(self):
        super(Visitor, self).__init__()

    def visit_stmt(self, node):
        for stmt in node.stmts:
            self.visit(stmt)


class TestInt(unittest.TestCase):
    def test_1(self):
        prg1 = "x := 10; print_state"
        # test parser
        ast1 = ast.parse_string(prg1)
        interp = wlang.int.Interpreter()
        st = wlang.int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(st)
        # x is defined
        self.assertIn('x', st.env)
        # x is 10
        self.assertEquals(st.env['x'], 10)
        # no other variables in the state
        self.assertEquals(len(st.env), 1)

    def test_2(self):
        my_visitor = Visitor()
        prg1 = """a := 1;
            b := 2;
            c := a + b;
            d := a - b;
            e := a * b;
            f := a / d;
            print_state"""
        prg2 = """a := 1;
            b := 2;
            c := a + b;
            d := a - b;
            e := a * b;
            f := a / d;
            print_state"""
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_3(self):
        my_visitor = Visitor()
        prg1 = """if 2 > 1 and 3 > 1 then a := 1"""
        prg2 = "a := 1"
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_4(self):
        my_visitor = Visitor()
        prg1 = """if 2 > 1 or 3 < 1 then a := 1"""
        prg2 = "a := 1"
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_5(self):
        my_visitor = Visitor()
        prg1 = """if 2 >= 1 and not 3 < 1 then a := 1"""
        prg2 = "a := 1"
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_6(self):
        my_visitor = Visitor()
        prg1 = """if true or false then a := 1 else b := 1"""
        prg2 = "a := 1"
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_7(self):
        my_visitor = Visitor()
        prg1 = """skip"""
        prg2 = "a := 1"
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_8(self):
        my_visitor = Visitor()
        prg1 = """a := 0;
            while inv (a < 3) and true do {a := a + 1}"""
        prg2 = "a := 1"
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_9(self):
        my_visitor = Visitor()
        prg1 = """a := 0;
            while (a < 3) or false do {a := a + 1}"""
        prg2 = """a := 0;
            while (a < 3) or false do {a := a + 1}"""
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_10(self):
        my_visitor = Visitor()
        prg1 = """a := 0;
            assume a = -1"""
        prg2 = """a := 0;
            assume a = -1"""
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_11(self):
        my_visitor = Visitor()
        prg1 = """a := 1;
            b := 2;
            havoc a, b"""
        prg2 = """a := 1;
            b := 2;
            havoc a, b"""
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_12(self):
        my_visitor = Visitor()
        prg1 = """a := 1;
            assert a = 1"""
        prg2 = "a := 1"
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_13(self):
        my_visitor = Visitor()
        prg1 = """a := 1;
            assert a = 2"""
        prg2 = """a := 1;
            assert a = 2"""
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_14(self):
        my_visitor = Visitor()
        prg1 = """print_state"""
        prg2 = """print_state"""
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_15(self):
        my_visitor = Visitor()
        prg1 = """a := 1"""
        prg2 = """a := 1"""
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        self.assertEqual(ast1, ast2)
        self.assertIsNotNone(ast1)
        repr(ast1)
        my_visitor.visit(ast1)
        return ast1

    def test_16(self):
        exp = ast.Exp('-', ['1', '2'])
        exp.is_binary()

    def test_17(self):
        pv = ast.PrintVisitor(None)
        pv.visit_StmtList(ast.StmtList(None))

    def test_18(self):
        ct = ast.Const(1)
        repr(ct)
        str(ct)
        hash(ct)

    def test_19(self):
        my_visitor = Visitor()
        ivr = ast.IntVar('a := 1')
        my_visitor.visit(ivr)
        repr(ivr)
        str(ivr)
        hash(ivr)

    def test_20(self):
        prg1 = "skip"
        ast1 = ast.parse_string(prg1)
        my_visitor = Visitor()
        my_visitor.visit(ast1)

    def test_21(self):
        prg = "a := 1"
        ast1 = ast.parse_string(prg)
        lang = parser.WhileLangSemantics()
        lang_methods = [method for method in dir(while_lang)
                        if callable(getattr(while_lang, method))
                        if not method.startswith('_')]
        for method in lang_methods:
            getattr(lang, method)(ast1)

    def test_22(self):
        prg = """a := 1;
            b := 2;
            c := a + b;
            d := a - b;
            e := a * b;
            f := a / d"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_23(self):
        prg = """if 2 > 1 and 3 > 1 then a := 1"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_24(self):
        prg = """if 2 >= 1 or 3 < 1 then a := 1"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_25(self):
        prg = """if 2 <= 1 and not 3 < 1 then a := 1"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_26(self):
        prg1 = """a := 1;
            if a < 2 then skip"""
        ast1 = ast.parse_string(prg1)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_27(self):
        prg = """a := 0;
            while (a < 3) and (a <= 3) do {a := a + 1}"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_28(self):
        prg = """a := 0;
            assume a = -1"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_29(self):
        prg = """a := 1;
            b := 2;
            havoc a, b"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_30(self):
        prg = """a := 1;
            assert a = 1"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_31(self):
        prg = """print_state"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_32(self):
        prg = """if 2 < 1 then a := 1 else a := -1"""
        ast1 = ast.parse_string(prg)
        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(ast1)

    def test_33(self):
        state = int.State()
        state.__repr__()

    def test_34(self):
        int1 = int._parse_args()
        self.assertIsNotNone(int1)

    def test_35(self):
        prg = "a := 1"
        ast1 = ast.parse_string(prg)
        intVar = ast.IntVar(ast1)
        intVar.__str__()
        intVar.__repr__()
        intVar.__hash__()

    def test_36(self):
        file = "wlang/test1.prg"
        ast1 = ast.parse_file(file)

    def test_37(self):
        prg1 = "if true then a := 1"
        ast1 = ast.parse_string(prg1)
        my_visitor = Visitor()
        my_visitor.visit(ast1)

    def test_38(self):
        ...


# For those cannot be covered:
# Int.py: 75, for RelExp, it is impossible to assert False.
# parse.py: 118, for _stmt_, it is impossible to return self.error.
# parse.py: 268, for _bfactor_, it is impossible to return self.error.

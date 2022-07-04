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
from . import ast, sym
import z3


class TestSym (unittest.TestCase):
    def test_one(self):
        prg1 = "havoc x; assume x > 10; assert x > 15"
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 1)

    def test_two(self):
        prg1 = """
              havoc x, y;
              p := x + y; q := x - y;
              m := x * y; n := x / y;
              if p > 10 or q < 5 then p := p - 1 else p := p + 1;
              while m >= 10 and n <= 5 do {m := m - 2; n := n + 3}
              """
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 6)

    def test_three(self):
        prg1 = """
              havoc p, x;
              assume p = -1;
              havoc m,n;
              assert x = 3;
              if not p > x then skip;
              q := 6;
              if q > 7 then q := 10
              """
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 1)

    def test_three(self):
        prg1 = """
              havoc p, x;
              assume p = -1;
              havoc m,n;
              assert x = 3;
              if not p > x then skip;
              q := 6;
              if q > 7 then q := 10
              """
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 1)

    def test_four(self):
        prg1 = """
              havoc x;
              assume x > 10;
              assert x < 15"
              y := 1;
              print_state y
              assert y = 3;
              asset y = 6;
              """
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 1)

    def test_five(self):
        prg1 = """
              x := 10;
              y := 20;
              assume x > 5 or true;
              assert y < 15 or true;
              x:=10; y := 11;
              assert y = x
              """
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 0)

    def test_six(self):
        prg1 = """
              x:=10; y := 11;
              assume y = x
              """
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 0)

    def test_seven(self):
        prg1 = """
              x:=10; y := 11;
              print_state y
              """
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        st.pick_concrete()
        self.assertEquals(len(out), 1)

    def test_eight(self):
        solver = z3.Solver()
        state = sym.SymState(solver)
        repr(state)
        print(state)
        state.add_pc(z3.BoolVal(True))
        x = z3.Int("x")
        y = z3.Int("y")
        state.add_pc(x > y)
        self.assertIsNotNone(state.pick_concrete())

    def test_nine(self):
        solver = z3.Solver()
        state = sym.SymState(solver)
        state.add_pc(z3.BoolVal(False))
        state.add_pc(z3.BoolVal(True))
        self.assertIsNone(state.pick_concrete())

    def test_ten(self):
        solver = z3.Solver()
        state = sym.SymState(solver)
        state.add_pc(z3.BoolVal(False))
        state.add_pc(z3.BoolVal(True))
        state.is_error()
        state.to_smt2()
        self.assertIsNone(state.pick_concrete())

    def test_eleven(self):
        prg1 = """
              x := 10;
              y := 20;
              while x > 5 do x := x - 1
              """
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 1)

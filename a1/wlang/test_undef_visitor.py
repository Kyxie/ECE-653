import unittest

from . import ast, undef_visitor


class TestUndefVisitor(unittest.TestCase):
    def test1(self):
        prg1 = "x := 10; y := x + z"
        ast1 = ast.parse_string(prg1)

        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        # UNCOMMENT to run the test
        ## self.assertEquals (set ([ast.IntVar('z')]), uv.get_undefs ())

    def test_2(self):
        prg1 = """a := 1;
            b := 2;
            c := a + b;
            d := a - b;
            e := a * b;
            f := a / d;
            print_state"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_3(self):
        prg1 = """if 2 > 1 and 3 > 1 then a := 1"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_4(self):
        prg1 = """if 2 > 1 or 3 < 1 then a := 1"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_5(self):
        prg1 = """if 2 >= 1 and not 3 < 1 then a := 1"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_6(self):
        prg1 = """if true or false then a := 1 else b := 1"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_7(self):
        prg1 = """skip"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_8(self):
        prg1 = """a := 0;
            while inv (a < 3) and true do {a := a + 1}"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_9(self):
        prg1 = """a := 0;
            while (a < 3) or false do {a := a + 1}"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_10(self):
        prg1 = """a := 0;
            assume a = -1"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_11(self):
        prg1 = """a := 1;
            b := 2;
            havoc a, b"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_12(self):
        prg1 = """a := 1;
            assert a = 1"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_13(self):
        prg1 = """a := 1;
            assert a = 2"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_14(self):
        prg1 = """print_state"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

    def test_15(self):
        prg1 = """a := 1"""
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(
            set([ast.IntVar('c'), ast.IntVar('e')]), uv.get_undefs())

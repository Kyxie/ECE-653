import unittest

from . import ast, stats_visitor


class TestStatsVisitor(unittest.TestCase):
    def test_one(self):
        prg1 = "x := 10; print_state"
        ast1 = ast.parse_string(prg1)

        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        # UNCOMMENT to run the test
        self.assertEquals(sv.get_num_stmts(), 2)
        self.assertEquals(sv.get_num_vars(), 1)

    def test_2(self):
        prg1 = """a := 1;
            b := 2;
            c := a + b;
            d := a - b;
            e := a * b;
            f := a / d;
            print_state"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_3(self):
        prg1 = """if 2 > 1 and 3 > 1 then a := 1"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_4(self):
        prg1 = """if 2 > 1 or 3 < 1 then a := 1"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_5(self):
        prg1 = """if 2 >= 1 and not 3 < 1 then a := 1"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_6(self):
        prg1 = """if true or false then a := 1 else b := 1"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_7(self):
        prg1 = """skip"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_8(self):
        prg1 = """a := 0;
            while inv (a < 3) and true do {a := a + 1}"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_9(self):
        prg1 = """a := 0;
            while (a < 3) or false do {a := a + 1}"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_10(self):
        prg1 = """a := 0;
            assume a = -1"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_11(self):
        prg1 = """a := 1;
            b := 2;
            havoc a, b"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_12(self):
        prg1 = """a := 1;
            assert a = 1"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_13(self):
        prg1 = """a := 1;
            assert a = 2"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_14(self):
        prg1 = """print_state"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

    def test_15(self):
        prg1 = """a := 1"""
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 20)
        self.assertEquals(sv.get_num_vars(), 6)

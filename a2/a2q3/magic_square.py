r'''
Date: 2022-05-05 14:52:01
LastEditors: Kunyang Xie
LastEditTime: 2022-07-04 18:08:19
'''
'''Magic Square

https://en.wikipedia.org/wiki/Magic_square

A magic square is a n * n square grid filled with distinct positive integers in
the range 1, 2, ..., n^2 such that each cell contains a different integer and
the sum of the integers in each row, column, and diagonal is equal.

'''




from z3 import *
def solve_magic_square(n, r, c, val):
    solver = Solver()

    X = []
    for i in range(n):
        line = []
        for j in range(n):
            ele = Int("x_%s_%s" % (i, j))
            line.append(ele)
        X.append(line)

    c1 = []
    for i in range(n):
        for j in range(n):
            c1.append(And(1 <= X[i][j], X[i][j] <= pow(n, 2)))

    temp = []
    for i in range(n):
        for j in range(n):
            temp.append(X[i][j])
    c2 = [Distinct(temp)]

    c3 = []
    for i_1 in range(n):
        for i_2 in range(n):
            c3.append(Sum(X[i_1]) == Sum(X[i_2]))

    c4 = [Sum([X[i][j] for i in range(n)]) == Sum(X[0]) for j in range(n)]
    c5 = [Sum([X[i][i] for i in range(n)]) == Sum(X[0])]
    c6 = [Sum([X[i][n - i - 1] for i in range(n)]) == Sum(X[0])]
    c7 = [X[r][c] == val]

    c8 = c1 + c2 + c7 + c3 + c4 \
        + c5 + c6

    solver.add(c8)

    if solver.check() == sat:
        mod = solver.model()
        res = [[mod.evaluate(X[i][j]).as_long() for j in range(n)]
               for i in range(n)]
        return res
    else:
        return None


def print_square(square):
    '''
    Prints a magic square as a square on the console
    '''
    n = len(square)

    assert n > 0
    for i in range(n):
        assert len(square[i]) == n

    for i in range(n):
        line = []
        for j in range(n):
            line.append(str(square[i][j]))
        print('\t'.join(line))


def puzzle(n, r, c, val):
    res = solve_magic_square(n, r, c, val)
    if res is None:
        print('No solution!')
    else:
        print('Solution:')
        print_square(res)


if __name__ == '__main__':
    n = 3
    r = 1
    c = 1
    val = 5
    puzzle(n, r, c, val)

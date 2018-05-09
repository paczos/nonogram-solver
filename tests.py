import pytest

from main import Nonogram, Solver

grid_expected = [
    ([
         [False, False, True, True, True],
         [False, False, False, True, True],
         [False, False, False, False, True],
         [True, True, True, False, False],
         [True, True, True, False, True]
     ], True),
    ([
         [True, False, True, True, True],
         [False, False, False, True, True],
         [False, False, False, False, True],
         [False, True, True, False, False],
         [True, True, True, False, True]
     ], False)
]


def get_nonogram():
    column_rules = {0: [2], 1: [2], 2: [1, 2], 3: [2], 4: [3, 1]}
    row_rules = {0: [3], 1: [2], 2: [1], 3: [3], 4: [3, 1]}

    return Nonogram(column_rules, row_rules)


@pytest.mark.parametrize('grid,expected', grid_expected)
def test_valid(grid, expected):
    nonogram = get_nonogram()
    nonogram._set_grid(grid)

    assert nonogram.is_valid() == expected


def test_solver():
    nonogram = get_nonogram()
    s = Solver(nonogram, nonogram.row_rules)

    solution = [
        [False, False, True, True, True],
        [False, False, False, True, True],
        [False, False, False, False, True],
        [True, True, True, False, False],
        [True, True, True, False, True]
    ]
    assert s.solve().grid == solution


def test_smiley():
    row_rules = {0: [4],
                 1: [6],
                 2: [2, 2, 2],
                 3: [8],
                 4: [1, 4, 1],
                 5: [2, 2],
                 6: [6],
                 7: [4],}
    column_rules = {0: [4],
                    1: [3,2],
                    2: [2,2,2],
                    3: [5,2],
                    4: [5,2],
                    5: [2,2,2],
                    6: [3,2],
                    7: [4],}
    nonogram = Nonogram(column_rules, row_rules, 8)
    s = Solver(nonogram, row_rules)
    s.solve().print()

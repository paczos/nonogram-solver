import sys

import pytest

from main import Nonogram, DFS, AStar, BFS

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
    s = DFS(nonogram, nonogram.row_rules)

    solution = [
        [False, False, True, True, True],
        [False, False, False, True, True],
        [False, False, False, False, True],
        [True, True, True, False, False],
        [True, True, True, False, True]
    ]
    assert s.solve().grid == solution


def test_paper():
    row_rules = {0: [2],
                 1: [1, 1],
                 2: [4],
                 3: [4], }
    column_rules = {0: [3],
                    1: [1, 2],
                    2: [4],
                    3: [2], }
    nonogram = Nonogram(column_rules, row_rules, 4)
    s = DFS(nonogram, row_rules)
    s.solve().print()


def test_5x5_w_DFS():
    row_rules = {0: [4],
                 1: [2, 2],
                 2: [1],
                 3: [2],
                 4: [2], }
    column_rules = {0: [2],
                    1: [2],
                    2: [1],
                    3: [2, 2],
                    4: [4],
                    }
    nonogram = Nonogram(column_rules, row_rules, 5)
    s = DFS(nonogram, row_rules)
    s.solve().print()


def test_5x5_w_BFS():
    row_rules = {0: [4],
                 1: [2, 2],
                 2: [1],
                 3: [2],
                 4: [2], }
    column_rules = {0: [2],
                    1: [2],
                    2: [1],
                    3: [2, 2],
                    4: [4],
                    }
    nonogram = Nonogram(column_rules, row_rules, 5)
    s = BFS(nonogram, row_rules)
    s.solve().print()


def test_5x5_w_AStar():
    row_rules = {0: [4],
                 1: [2, 2],
                 2: [1],
                 3: [2],
                 4: [2], }
    column_rules = {0: [2],
                    1: [2],
                    2: [1],
                    3: [2, 2],
                    4: [4],
                    }
    nonogram = Nonogram(column_rules, row_rules, 5)
    s = AStar(nonogram, row_rules)
    s.solve().print()


def test_5x5_tetri_DFS():
    row_rules = {0: [3],
                 1: [2],
                 2: [1],
                 3: [1, 2],
                 4: [4], }
    column_rules = {0: [3],
                    1: [2, 2],
                    2: [1, 1],
                    3: [2],
                    4: [2],
                    }
    nonogram = Nonogram(column_rules, row_rules, 5)
    s = DFS(nonogram, row_rules)
    s.solve().print()


def test_5x5_tetri_BFS():
    row_rules = {0: [3],
                 1: [2],
                 2: [1],
                 3: [1, 2],
                 4: [4], }
    column_rules = {0: [3],
                    1: [2, 2],
                    2: [1, 1],
                    3: [2],
                    4: [2],
                    }
    nonogram = Nonogram(column_rules, row_rules, 5)
    s = BFS(nonogram, row_rules)
    s.solve().print()


def test_5x5_tetri_AStar():
    row_rules = {0: [3],
                 1: [2],
                 2: [1],
                 3: [1, 2],
                 4: [4], }
    column_rules = {0: [3],
                    1: [2, 2],
                    2: [1, 1],
                    3: [2],
                    4: [2],
                    }
    nonogram = Nonogram(column_rules, row_rules, 5)
    s = AStar(nonogram, row_rules)
    s.solve().print()


def test_8x8_smiley_DFS():
    row_rules = {0: [4],
                 1: [6],
                 2: [2, 2, 2],
                 3: [8],
                 4: [1, 4, 1],
                 5: [2, 2],
                 6: [6],
                 7: [4], }
    column_rules = {0: [4],
                    1: [3, 2],
                    2: [2, 2, 2],
                    3: [5, 2],
                    4: [5, 2],
                    5: [2, 2, 2],
                    6: [3, 2],
                    7: [4], }
    nonogram = Nonogram(column_rules, row_rules, 8)
    s = DFS(nonogram, row_rules)
    s.solve().print()


def test_8x8_smiley_BFS():
    row_rules = {0: [4],
                 1: [6],
                 2: [2, 2, 2],
                 3: [8],
                 4: [1, 4, 1],
                 5: [2, 2],
                 6: [6],
                 7: [4], }
    column_rules = {0: [4],
                    1: [3, 2],
                    2: [2, 2, 2],
                    3: [5, 2],
                    4: [5, 2],
                    5: [2, 2, 2],
                    6: [3, 2],
                    7: [4], }
    nonogram = Nonogram(column_rules, row_rules, 8)
    s = BFS(nonogram, row_rules)
    s.solve().print()


def test_8x8_smiley_AStar():
    row_rules = {0: [4],
                 1: [6],
                 2: [2, 2, 2],
                 3: [8],
                 4: [1, 4, 1],
                 5: [2, 2],
                 6: [6],
                 7: [4], }
    column_rules = {0: [4],
                    1: [3, 2],
                    2: [2, 2, 2],
                    3: [5, 2],
                    4: [5, 2],
                    5: [2, 2, 2],
                    6: [3, 2],
                    7: [4], }
    nonogram = Nonogram(column_rules, row_rules, 8)
    s = AStar(nonogram, row_rules)
    s.solve().print()


def test_8x8_compare_AStar():
    row_rules = {0: [3, 2],
                 1: [4, 2],
                 2: [1, 1, 2],
                 3: [1, 2, 1],
                 4: [1, 3, 2],
                 5: [3, 2],
                 6: [7],
                 7: [2, 4], }
    column_rules = {0: [1, 2, 1],
                    1: [2, 2],
                    2: [7],
                    3: [1, 4],
                    4: [2, 4],
                    5: [1, 2],
                    6: [3, 4],
                    7: [7], }
    nonogram = Nonogram(column_rules, row_rules, 8)
    s = AStar(nonogram, row_rules)
    s.solve().print()


def test_8x8_compare_BFS():
    row_rules = {0: [3, 2],
                 1: [4, 2],
                 2: [1, 1, 2],
                 3: [1, 2, 1],
                 4: [1, 3, 2],
                 5: [3, 2],
                 6: [7],
                 7: [2, 4], }
    column_rules = {0: [1, 2, 1],
                    1: [2, 2],
                    2: [7],
                    3: [1, 4],
                    4: [2, 4],
                    5: [1, 2],
                    6: [3, 4],
                    7: [7], }
    nonogram = Nonogram(column_rules, row_rules, 8)
    s = BFS(nonogram, row_rules)
    s.solve().print()


def test_8x8_compare_DFS():
    row_rules = {0: [3, 2],
                 1: [4, 2],
                 2: [1, 1, 2],
                 3: [1, 2, 1],
                 4: [1, 3, 2],
                 5: [3, 2],
                 6: [7],
                 7: [2, 4], }
    column_rules = {0: [1, 2, 1],
                    1: [2, 2],
                    2: [7],
                    3: [1, 4],
                    4: [2, 4],
                    5: [1, 2],
                    6: [3, 4],
                    7: [7], }
    nonogram = Nonogram(column_rules, row_rules, 8)
    s = DFS(nonogram, row_rules)
    s.solve().print()


def test_9x9_AStar():
    sys.setrecursionlimit(30000)
    row_rules = {0: [3, 1],
                 1: [3, 2],
                 2: [3, 3],
                 3: [0],
                 4: [1],
                 5: [3, 1],
                 6: [5, 3],
                 7: [3, 1],
                 8: [1], }
    column_rules = {0: [1],
                    1: [3, 3],
                    2: [3, 5],
                    3: [3, 3],
                    4: [1],
                    5: [0],
                    6: [3, 1],
                    7: [2, 3],
                    8: [1, 1], }
    nonogram = Nonogram(column_rules, row_rules, 9)
    s = AStar(nonogram, row_rules)
    # s.solve().print()  # TAKES TOO LONG TIME, FAILES TO EXECUTE WITHIN A REASONABLE TIME


def test_dog_AStar():
    sys.setrecursionlimit(30000)
    row_rules = {0: [2, 1],
                 1: [6],
                 2: [1, 1, 1],
                 3: [5],
                 4: [1, 1, 1],
                 5: [8],
                 6: [6],
                 7: [2, 2],
                 8: [1, 1],
                 9: [9],
                 }

    column_rules = {0: [1],
                    1: [4, 1],
                    2: [1, 3, 1],
                    3: [3, 2, 1],
                    4: [1, 7],
                    5: [3, 3, 1],
                    6: [2, 2, 1],
                    7: [3, 1],
                    8: [5],
                    9: [2, 1],
                    }

    bobo = Nonogram(column_rules, row_rules, 10)
    s = AStar(bobo, row_rules)  # other algorithms are too slow for this
    # s.solve().print() # TAKES TOO LONG TIME, FAILES TO EXECUTE WITHIN A REASONABLE TIME


def test_duck_AStar():
    row_rules = {0: [3],
                 1: [5],
                 2: [4, 3],
                 3: [7],
                 4: [5],
                 5: [3],
                 6: [5],
                 7: [1, 8],
                 8: [3, 3, 3],
                 9: [7, 3, 2],
                 10: [5, 4, 2],
                 11: [8, 2],
                 12: [10],
                 13: [2, 3],
                 14: [6],
                 }

    column_rules = {
        0: [3],
        1: [4],
        2: [5],
        3: [4],
        4: [5],
        5: [6],
        6: [3, 2, 1],
        7: [2, 2, 5],
        8: [4, 2, 6],
        9: [8, 2, 3],
        10: [8, 2, 1, 1],
        11: [2, 6, 2, 1, ],
        12: [4, 6],
        13: [2, 4],
        14: [1],
    }
    nonogram = Nonogram(column_rules, row_rules, 15)
    s = AStar(nonogram, row_rules)  # other
    # s.solve().print() # TAKES TOO LONG TIME, FAILES TO EXECUTE WITHIN A REASONABLE TIME

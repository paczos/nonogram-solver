import sys
from itertools import groupby


class Nonogram:
    # zero-indexed
    size = 5
    column_rules = dict()
    row_rules = dict()
    grid = list()

    def __init__(self, column_rules, row_rules):
        self.column_rules = column_rules
        self.row_rules = row_rules
        self.grid = [[False for _ in range(self.size)] for _ in range(self.size)]

    def print(self):
        print()
        for row in self.grid:
            print(' | '.join(map(lambda x: 'X' if x else ' ', row)))

    def set_cell(self, x, y, value):
        try:
            self.grid[x][y] = value
        except IndexError:
            print('Out of range.')

    def _set_grid(self, grid):
        self.grid = grid

    def is_valid(self):
        def check_sequence(seq, checker):
            assert checker == list(map(len, filter(any, [list(g) for k, g in groupby(seq)])))

        try:
            for i in range(self.size):
                check_sequence(self.get_column(i), self.column_rules[i])
                check_sequence(self.get_row(i), self.row_rules[i])
        except AssertionError:
            return False

        return True

    def get_row(self, index):
        return self.grid[index]

    def get_column(self, index):
        return [row[index] for row in self.grid]


class Solver:
    row_rules = dict()
    nonogram = None

    def __init__(self, nonogram, row_rules):
        if not isinstance(nonogram, Nonogram):
            raise ValueError('you have to pass an instance of nonogram')

        self.nonogram = nonogram
        self.row_rules = row_rules

    def fill_row(self, index, rules):
        pass

    def solve(self):
        for i in range(self.nonogram.size):
            self.fill_row()


class BFS(Solver):
    pass


class AStar(Solver):
    pass


def main():
    nono = Nonogram({}, {})
    nono.print()
    print(nono.is_valid())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()


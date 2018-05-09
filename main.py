import sys
from itertools import groupby, combinations_with_replacement, repeat


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

    def row_combinations(self, rules):
        """generate all possibilities to insert spaces between occupied cells"""
        rules_groups_count = len(rules)
        size = self.nonogram.size
        space_occupied_by_marked_cells = sum(rules)
        spaces_to_insert = size - space_occupied_by_marked_cells - (rules_groups_count - 1)
        places_to_insert_count = rules_groups_count + 1

        # generate all possibilities that one or more additional spaces can be inserted between groups
        cs = combinations_with_replacement(range(places_to_insert_count), spaces_to_insert)

        for c in cs:
            def create_buckets(rs):
                rs_buckets = list()
                for idx, r in enumerate(rs):
                    if idx == 0:
                        rs_buckets.append(0)
                        rs_buckets.append(r)
                    else:
                        rs_buckets.append(-1)
                        rs_buckets.append(r)
                rs_buckets.append(0)
                return rs_buckets

            extended_rules = create_buckets(rules)
            for i in c:
                extended_rules[i * 2] -= 1

            grid_compatible = list()
            for entry in extended_rules:
                if entry < 0:
                    grid_compatible.extend(repeat(False, abs(entry)))
                else:
                    grid_compatible.extend(repeat(True, abs(entry)))

            yield grid_compatible

    def fill_row(self, idx, entries):
        self.nonogram.grid[idx] = entries

    def solve_row(self, idx):
        for c in self.row_combinations(self.row_rules[idx]):
            self.fill_row(idx, c)
            if idx + 1 == self.nonogram.size:
                yield self.nonogram
            else:
                deeper = self.solve_row(idx + 1)
                yield from deeper

    def solve(self):
        for ct, solution in enumerate(self.solve_row(0)):
            print('suggested solution', ct)
            solution.print()
            is_valid = solution.is_valid()
            print('valid:', is_valid)
            if is_valid:
                return solution.grid


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

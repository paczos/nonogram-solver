"""
Paweł Paczuski, Dmytro Ievseienko, EARIN 18L P2.2
"""

import sys
from collections import deque
from copy import deepcopy
from itertools import groupby, combinations_with_replacement, repeat
from queue import PriorityQueue


class Nonogram:
    size = None
    column_rules = dict()
    row_rules = dict()
    grid = list()

    def __init__(self, column_rules, row_rules, size=5):
        self.size = size
        self.column_rules = column_rules
        self.row_rules = row_rules
        self.grid = [[False for _ in range(self.size)] for _ in range(self.size)]

    def print(self):
        print()
        for row in self.grid:
            print(' | '.join(map(lambda x: '◼' if x else ' ', row)))

    # setters
    def set_cell(self, x, y, value):
        try:
            self.grid[x][y] = value
        except IndexError:
            print('Unable to set value for a cell: one of indexes is ut of range.')

    def set_row(self, idx, row):
        self.grid[idx] = row

    def _set_grid(self, grid):
        """Set the whole grid - used in tests."""
        self.grid = grid

    # getters
    def get_row(self, index):
        return self.grid[index]

    def get_column(self, index):
        return [row[index] for row in self.grid]

    # validation
    def check_sequence(self, seq, checker):
        assert checker == self.group_cells(seq)

    @staticmethod
    def group_cells(sequence):
        return list(map(len, filter(any, [list(g) for k, g in groupby(sequence)])))

    def is_valid(self):
        try:
            for i in range(self.size):
                self._is_line_valid('row', i)
                self._is_line_valid('column', i)
        except AssertionError:
            return False

        return True

    def _is_line_valid(self, line_type, line_index, shout=True):
        """Check whether line (row or column) is valid."""
        assert line_type == 'row' or line_type == 'column'

        try:
            self.check_sequence(
                getattr(self, 'get_{}'.format(line_type))(line_index),
                getattr(self, '{}_rules'.format(line_type))[line_index]
            )
        except AssertionError:
            if shout:
                raise
            return False

        return True


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

    def search_space_elems(self, idx):
        raise NotImplementedError('must be implemented by a subclass')

    def solve(self):
        for ct, solution in enumerate(self.search_space_elems(0)):
            print('suggested solution', ct)
            solution.print()
            is_valid = solution.is_valid()
            print('valid:', is_valid)
            if is_valid:
                return solution


class DFS(Solver):
    def search_space_elems(self, idx):
        for c in self.row_combinations(self.row_rules[idx]):
            self.nonogram.set_row(idx, c)
            if idx + 1 == self.nonogram.size:
                yield self.nonogram
            else:
                deeper = self.search_space_elems(idx + 1)
                yield from deeper


class BFS(Solver):
    def __init__(self, nonogram, row_rules):
        super().__init__(nonogram, row_rules)
        self.queue = deque()

    def search_space_elems(self, idx=0, grid=None):
        global c
        queue = self.queue
        if grid is None:  # generating first solution grid
            grid = list()
            for i in range(self.nonogram.size):
                grid.append(next(self.row_combinations(self.row_rules[i])))

        for i, c in enumerate(self.row_combinations(self.row_rules[idx])):
            grid[idx] = c
            queue.append((idx + 1, deepcopy(grid)))

        while queue:
            (lrow, lel) = queue.popleft()
            self.nonogram.grid = lel
            print('q size', len(queue))
            yield self.nonogram
            if lrow != self.nonogram.size:
                yield from self.search_space_elems(lrow, lel)


class AStar(Solver):
    def __init__(self, nonogram, row_rules):
        super().__init__(nonogram, row_rules)
        self.queue = PriorityQueue()

    def search_space_elems(self, idx=0, grid=None):
        global c
        queue = self.queue
        if grid is None:  # generating first solution grid
            grid = list()
            for i in range(self.nonogram.size):
                grid.append(next(self.row_combinations(self.row_rules[i])))

        for i, c in enumerate(self.row_combinations(self.row_rules[idx])):
            grid[idx] = c
            weight = (self.count_invalid_groups(grid))
            copy = deepcopy(grid)
            assert len(copy) == self.nonogram.size
            queue.put((weight, (idx, copy)))

        while queue:
            (_, (lrow, lel)) = queue.get()
            self.nonogram.grid = lel
            yield self.nonogram
            if lrow + 1 < self.nonogram.size:
                yield from self.search_space_elems(lrow + 1, lel)

    def count_invalid_groups(self, grid):  # heuristic function
        self.nonogram.grid = grid
        not_fit_count = 0
        for cdx in range(self.nonogram.size):
            column = self.nonogram.get_column(cdx)
            column_groups = self.nonogram.group_cells(column)
            column_rules = self.nonogram.column_rules[cdx]
            fitting = list(map(lambda x: x[0] == x[1], zip(column_rules, column_groups))).count(False)
            not_fit_count += fitting
        return not_fit_count


def main():
    nono = Nonogram({}, {})
    nono.print()
    print(nono.is_valid())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

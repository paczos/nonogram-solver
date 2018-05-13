# EARIN Miniproject 2
###### Paweł Paczuski, Dmytro Ievseienko


## Nonogram - formal rules
* there is a grid where each cell can be filled with "X" or "◼"
* each cell and each row has a set of rules
* rules are defined as a numbers of continuous ◼'es in a group:
    * example: rule 2, 1 defines two ◼ followed by a _space_ and another ◼, where _space_ can be of any number of X'es but not less than one.
* there should be one solution to the Nongram

## Puzzle space and Search space

## Heuristic function

# !TODO DESCRIBE

## Performance of algorithms

| Nonogram | Size |         DFS        |        BFS          |      A star     |
| -------- | ---- | ------------------ | ------------------- | --------------- |
| Smiley   |  8x8 | 560ms, 1147 visits | 2561ms, 1812 visits | 26ms, 11 visits |
| ??????   |  8x8 | 20414ms, 3775 visits | n/a - RecursionLimit, >2000 visits | 600ms, 364 visits |




## Implementation details

### class Nonogram

This class is responsible for:

* Storing the grid
* Basic operations on the grid
* Validation - both full and partial

And it also contains helper functions for validation

### class Solver

This class provides the solving "framework"
It implements set of helper functions and an interface for our tests.

One of the basic helper method is `row_combinations` which generates valid combinations based on the row rules.
Generally speaking it generates plausible solutions for the row.

### Tests

Tests are build using `pytest` framework.


### Other
Times of execution are measured using this framework and a PyCharm testing tool.

OS: Ubuntu 17.04, processor: Intel Core i7 (6th gen)

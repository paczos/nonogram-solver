# EARIN Miniproject 2
###### Paweł Paczuski, Dmytro Ievseienko


## Nonogram - formal rules
* there is a grid where each cell can be filled with "X" or "◼"
* each cell and each row has a set of rules
* rules are defined as a numbers of continuous ◼'es in a group:
    * example: rule 2, 1 defines two ◼ followed by a _space_ and another ◼, where _space_ can be of any number of X'es but not less than one.
* The first solution that satisfies both row and column rules is returned (This does not always have to be the case, as one set of row and column rules would allow for many correct solutions. Determining whether a nonogram has a single or many solutions is also a NP-hard problem). 

## Puzzle space and Search space

A maximally large puzzle space would contain all possible fillings of the NxN grid. It would, however, be a waste of resources to analyze all, even solutions with no relation to the row and column rules. In order to make the space smaller, it is set up with respect to row rules. Elements of the search space are all solutions to the nonogram that have all rows filled with groups of ◼ generated according to row rules. Each element is correct with respect to the row rules, but not always according to the column rules. It is the goal of the algorithm to find among all elements of the search space ones that are also correct with respect to the column rules. 

Initially, a nonogram is filled with first suggestions for all rows. 

Neighbours of a state (descendants) in the tree of states at depth h are all states that contain proper combinations of cells in grid for h+1-th row. 


## Uninformed search
Using this interpretation of search space, DFS search algorithm tries to fix all rows except one, and looks for the solution by enumerating all possibilities. 
From BFSs' perspective, all possibilities with one row changed are validated, then the focus is shifted to another row. However, next visited node may differ with current one by more than one rows as the algorithm may move deeper in the tree.

Due to the nature of both algorithms, it would be expected that DFS is much more memory efficient, as a single instance of the grid can be mutated wisely, but the algorithm may find the solution using larger number of steps. BFS, on the other hand, should use more memory, but solve the nonogram using smaller number of steps.

## Informed search: A* and heuristic function
A* is used as a method to find the solution in a smaller number of steps. Possible solutions are generated similarly to the BFS and DFS, but the order of validating solutions is different. A priority queue is used to asses whether a possible solution should be expanded sooner or later. The priority is calculated using heuristic function.
### Heuristic function
Proposed heuristic function uses pieces information that are not used by uninformed search – column rules.  
The simplest possible heuristic function would count number of columns that are valid with respect to the column rules. This , however, does not convey enough information. The whole column is incorrect when only one pixel is placed improperly according to column rules.  
More advanced heuristic function simply counts total number of invalid groups that are placed incorrectly according to the column rules. This way solutions that require only small changes are placed first in the queue.  

#### Properties
* The heuristic function is **monotonous** because as one gets closer to the solution it returns smaller values. A better suggested solution has smaller number of invalid groups than a worse solution.
* The heuristic function is **admissible** because the returned number of invalid groups is always smaller or equal (when the only incorrect group is of length 1) to the number of steps required to find the correct solution.


## Performance of algorithms !TODO DESCRIBE, fill with times and iteration numbers @Dima

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

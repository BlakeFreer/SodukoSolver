# Sudoku Solver 
Solves Sudoku puzzles that do not require guessing.

## Usage
1. Download Cell.py, Grid.py and Solver.py into a directory
2. Download some sample grid puzzle files
3. Navigate in your Terminal / Command Prompt to the directory containing the .py files
4. Run ```python Solver.py [puzzle file path]```

## Terminology
Cell - The smallest unit on a Sudoku puzzle, can hold a single value

Grid - The 9x9 grid of cells that make up the puzzle

Row - A horizontal row of the grid containing 9 cells

Column - A vertical column of the grid containing 9 cells

3x3 Box - The 9x9 grid is divided into 9 sub-grids of 9 cells each
- Each cell, column and 3x3 box must contain each digit from 1-9

Peers - For any Cell, the Peers are the 20 cells that are in the same row, column or 3x3 box. If a specific digit appears in a cell, it cannot be placed in any of that cell's peers.

## Classes
### Cell
Cell has a set of "possible digits" - digits that the Cell could potentially hold.

### Grid
Grid holds a 9x9 2D array of cells. It provides methods for getting peer cells or finding the cells in a specific row, column or 3x3 box.

### Solver
Handles command line input and houses the solving method described below.

## Method of Solving
1. The puzzle file is read through to create a Grid object that holds the Cells. This array is populated by initializing cells either with a starting value or as empty, wiht a set of possible digits containing each digit 1 through 9.
2. The solved cells are iterated through. At each solved cell, it removes its value from its peers.
3. The rows, columns and 3x3 boxes are iterated through. At each one, every combination of unsolved cells is considered. If the union of possible digits from ```n``` unsolved cells is of length ```n```, then the digits in the union cannot be used in any of the other unsolved cells in the current row / column / 3x3. This is an extended, generalized use of the [Naked Pair](http://hodoku.sourceforge.net/en/tech_naked.php) and [Hidden Pair](http://hodoku.sourceforge.net/en/tech_hidden.php) strategies.
4. Whenever a cell's possible digits set is reduced to a single digit (in step 2 or 3), the cell becomes solved. This newly solved cell then removes its value from its peers. If this leads to another cell being solved, then the program recursively updates from that new cell, until all updates have been made and no new cells are solved.
5. Step 3 repeats until all of the Cells in the Grid become solved. This is determined by tracking how many unsolved cells remain. At this point, the program ends and displays the solved grid.

## Limitations
There are several puzzles that cannot be solved in this method, causing the program to endlessly loop over step 3. There are other strategies may need to be employed to solve specific cells before the recursive updating can continue making progress. There are too many strategies to implement that involved checking several cells, which would lead to lengthy code and worse performance. Please [email me](bkfreer10@gmail.com) if you find a way to generalize many strategies in a similar way to how I generalized the Naked Pair strategy to work with multiple cells.

## Takeaways
I started this mini-project to try to find an alternative to the traditional backtracking Sudoku algorithm, as I was unsatisfied by the guess-and-check style solution. However, through debugging my algorithms and trying different puzzles, I gained a much greater respect for the challenge of Sudoku puzzles and the various strategies that can be used to narrow in on a correct cell value. While I was not able to use analytical methods to completely solve every puzzle, I am content with how much I learned in algorithm design, file parsing and recursive functions.

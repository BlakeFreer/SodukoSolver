#! python

# Solves a Sudoku grid
# Author:   Blake Freer
# Date:     October 15, 2020

import Grid
import Cell
import argparse
from itertools import cycle, combinations

solves = []

def SolveRecursive(grid: Grid):
    global solves
    '''
    Iterate through each cell in the grid, and solve recursively from there if the cell is solved.
    '''

    # Stage 1: Remove all possible values from unsolved cells based on values of solved peers
    for c in grid.Get_All():
        if c.value:
            SolveFromCell(grid, c)
    
    # Stage 2: Cycle through the rows, columns and boxes to check for cell digit overlaps
    iteration = 0
    while grid.unsolved_cells > 0:
        for n in range(9):
            cur_cells = grid.Get_Box(n) if iteration == 0 else grid.Get_Row(n) if iteration == 1 else grid.Get_Col(n)
            for size in range(2, len(cur_cells)):
                for combo in combinations(cur_cells, size):
                    union = set.union(*map(set, [x.possible_digits for x in combo]))
                    if len(union) == size:
                        print(str(union) + " in",size,{0:"Box",1:"Row",2:"Column"}[iteration], n)
                        for cell in [x for x in cur_cells if x not in combo]:
                            print("checking ",cell.row,cell.column)
                            if cell.Eliminate_Digits(union):
                                grid.unsolved_cells -= 1
                                SolveFromCell(grid, cell)
        iteration += 1
        iteration %= 3

        print("\n"*4)
        print(grid.toString(True))
    
def SolveFromCell(grid: Grid, cell: Cell):
    '''
    Use the value of a solved cell to remove options from a peer cell.

    If a peer cell becomes solved, recursively solve from there. When no more cells are solved on a current branch, move to the next one in the parent branch.
    '''
    for c in grid.Get_Peers(cell):
        if c.Eliminate_Digits({cell.value}):
            grid.unsolved_cells -= 1
            SolveFromCell(grid, c)

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=
    """
    Solve a Sudoku puzzle

    Input:
        File should be a 9x9 grid of numbers.
        Empty cells should be represented by a 0 (zero).
        Do not separate digits with spaces, commas, etc.

    Output:
        Displays the solved grid.
        Grid is formatted in the same way as the input file, unless the --fancy flag is used

    Solving Method:
        The algorithm makes 2 passes through the whole board.

        On the first pass, solved cells are used to update unsolved cells by removing their
        value as a possible digit in their peers. If 8 digits are eliminated from an unsolved
        cell, that cell becomes solved and it updates its peers in a recursive fashion.

        On the second pass, unsolved cells are checked against their row, column, and 3x3 sub-
        grid. If there is a digit that can only be placed in the current cell (i.e. it has been
        eliminated from all the other cells in the row/column/3x3) then the cell is solved with
        that digit. This newly solved cell then recursively updates the possible digits of its
        peers using the same method as the first pass.
    """
    )
    parser.add_argument(
        'file',
        help='path to unsolved grid file'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='display step by step solution to the puzzle'
    )
    
    args = parser.parse_args()
    
    with open(args.file, 'r') as file:
        puzzle_string = file.read()

    # Remove whitespace from string
    puzzle_string = "".join(puzzle_string.split())
    # Remove | characters and replace . with 0
    puzzle_string = puzzle_string.replace("|", "")
    puzzle_string = puzzle_string.replace("+", "")
    puzzle_string = puzzle_string.replace("-", "")
    puzzle_string = puzzle_string.replace(".", "0")

    def Puzzle(p):
        g = Grid.Grid(p)

        if args.verbose:
            print("INITIAL\n"+g.toString(args.verbose))

        SolveRecursive(g)

        if args.verbose:
            print("\n".join(solves))
            print("\nFINAL")

        print(g.toString(args.verbose))
    
    for i in range(0, len(puzzle_string), 81):
        if len(puzzle_string) > 81:
            print("\nPuzzle", i//81)
        Puzzle(puzzle_string[i:i+81])

if __name__ ==  "__main__":
    main()


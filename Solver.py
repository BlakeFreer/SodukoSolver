#! python

# Solves a Sudoku grid
# Author:   Blake Freer
# Date:     October 15, 2020

import Grid
import Cell
import argparse

solves = []

def SolveRecursive(grid: Grid, log):
    global solves
    '''
    Iterate through each cell in the grid, and solve recursively from there if the cell is solved.
    '''

    # Stage 1: Remove all possible values from unsolved cells based on values of solved peers
    for c in grid.Get_All():
        if c.value:
            SolveFromCell(grid, c, log)

    # Stage 2: Check all unsolved cells against their row, column and 3x3. If there is a value
    # that can only be placed in this cell, solve it.

    for c in grid.Get_All():
        if not c.value:
            if c.Solve_By_Peers(grid):
                if log[0]:
                    solves.append("\n"+str(c)+" by peer digit option comparisons\n"+grid.toString(log[1]))
                SolveFromCell(grid, c, log)

    
def SolveFromCell(grid: Grid, cell: Cell, log):
    global solves
    '''
    Use the value of a solved cell to remove options from a peer cell.

    If a peer cell becomes solved, recursively solve from there. When no more cells are solved on a current branch, move to the next one in the parent branch.
    '''
    for c in grid.Get_Peers(cell):
        if c.Remove_Option(cell.value):
            if log[0]:
                solves.append("\n"+str(c)+" by digit elimination\n"+grid.toString(log[1]))
            SolveFromCell(grid, c, log)


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
    parser.add_argument(
        '--fancy',
        action='store_true',
        help='display the solved grid with grid lines and spacing'
    )
    
    args = parser.parse_args()
    g = Grid.Grid(args.file)

    if args.verbose:
        print("INITIAL\n"+g.toString(args.fancy))

    SolveRecursive(g, (args.verbose, args.fancy))

    if args.verbose:
        print("\n".join(solves))
        print("\nFINAL")

    print(g.toString(args.fancy))

if __name__ ==  "__main__":
    main()
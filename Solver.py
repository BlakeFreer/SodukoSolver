#! python

# Solves a Sudoku grid
# Author:   Blake Freer
# Date:     October 14, 2020

import Grid
import Cell
import argparse

solves = []

def SolveRecursive(grid: Grid, log: bool):
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
                if log:
                    solves.append("\n"+str(c)+" by peer digit option comparisons\n"+str(grid))
                SolveFromCell(grid, c, log)

    
def SolveFromCell(grid: Grid, cell: Cell, log: bool):
    global solves
    '''
    Use the value of a solved cell to remove options from a peer cell.

    If a peer cell becomes solved, recursively solve from there. When no more cells are solved on a current branch, move to the next one in the parent branch.
    '''
    for c in grid.Get_Peers(cell):
        if c.Remove_Option(cell.value):
            if log:
                solves.append("\n"+str(c)+" by digit elimination\n"+str(grid))
            SolveFromCell(grid, c, log)


def main():
    parser = argparse.ArgumentParser(description="Solve a Sudoku puzzle")
    parser.add_argument(
        'file',
        help='Path to unsolved grid file'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Display step by step solution to the puzzle'
    )
    
    args = parser.parse_args()
    g = Grid.Grid(args.file)

    if args.verbose:
        print("INITIAL\n"+str(g))

    SolveRecursive(g, args.verbose)

    if args.verbose:
        print("\n".join(solves))
        print("\nFINAL")

    print(g)

if __name__ ==  "__main__":
    main()
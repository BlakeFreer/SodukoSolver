#! python

# Solves a Sudoku grid
# Author:   Blake Freer
# Date:     October 14, 2020

import Grid
import Cell
import argparse

def SolveRecursive(grid: Grid, log: bool):
    '''
    Iterate through each cell in the grid once, and solve recursively from there if the cell is solved.
    '''
    for c in grid.Get_All():
        if c.value:
            SolveFromCell(grid, c, log)
    
def SolveFromCell(grid: Grid, cell: Cell, log: bool):
    '''
    Use the value of a solved cell to remove options from a peer cell.

    If a peer cell becomes solved, recursively solve from there. When no more cells are solved on a current branch, move to the next one in the parent branch.
    '''
    for c in grid.Get_Peers(cell):
        if c.Update(cell.value):
            if log:
                print(c)
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
        help='Display the order in which the cells are solved'
    )
    
    args = parser.parse_args()
    g = Grid.Grid(args.file)
    print(g)
    print()
    SolveRecursive(g, args.verbose)
    print()
    print(g)
    for c in g.Get_All():
        continue
        print(c)

if __name__ ==  "__main__":
    main()
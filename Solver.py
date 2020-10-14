# Solves a Sudoku grid
# Author:   Blake Freer
# Date:     October 14, 2020

from SudokuElements import Grid, Cell
import time

grid_file_path = "SampleGrids/Grid01.txt"

g = Grid(grid_file_path)

def Solve(grid: Grid):
    '''
    OBSELETE: Use Solve Recursive

    Solves a Sudoku grid by iterating through each cell and eliminating options in its peers.

    Known ineficiencies:
    
    The function may iterate through the 81 cells multiple times, meaning that the same option is removed from the same peers multiple times.
    
    The list of peer cells includes 4 cells that are a part of the cross and 3x3 box, so they are modified twice. This should be fixed with a better method in the Grid class.
    
    The function always solves from the next cell in the grid layout. It should start like this, but when a cell becomes solved, jump to it and solve from there, since it is where the most new information is available.
    '''

    while grid.unsolved_cells > 0:
        # Loop through all of the cells and update the neigbours
        for cur_cell in grid.Get_All():
            if cur_cell.value:
                # If the current cell is solved (aka has a value), then remove that
                # option from peers (cells in the same Cross or 3x3 box)
                for c in grid.Get_3x3(cur_cell) + grid.Get_Cross(cur_cell):
                    if c.Eliminate_Option(cur_cell.value):
                        grid.unsolved_cells -= 1
                        #print("Solved",c)
            else:
                pass

def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:{} args:[{}, {}] took: {:.4f} sec'.format(f.__name__, args, kw, te-ts))
        return result
    return timed

def SolveFromCell(grid: Grid, cell: Cell):
    '''
    Use the value of a solved cell to remove options from a peer cell.

    If a peer cell becomes solved, recursively solve from there. When no more cells are solved on a current branch, move to the next one in the parent branch.
    '''
    for c in grid.Get_Peers(cell):
        if c.Eliminate_Option(cell.value):
            SolveFromCell(grid, c)

#@timeit
def SolveRecursive(grid: Grid):
    '''
    Iterate through each cell in the grid once, and solve recursively from there if the cell is solved.
    '''
    for c in grid.Get_All():
        if c.value:
            SolveFromCell(grid, c)

@timeit
def rep(reps):
    for _ in range(reps):
        g = Grid(grid_file_path)
        SolveRecursive(g)

rep(10000)


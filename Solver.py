# Solves a Sudoku grid
# Author:   Blake Freer
# Date:     October 14, 2020

from SudokuElements import Grid

grid_file_path = "SampleGrids/Grid01.txt"

g = Grid(grid_file_path)

print(g)

def Solve(grid: Grid):
    '''
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
                        print("Solved",c)
            else:
                pass

Solve(g)
print("\n"+str(g))
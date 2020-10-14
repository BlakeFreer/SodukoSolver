# Container for the 9x9 grid of cells, providing methods for retrieving specific cells
# Author:   Blake Freer
# Date:     October 14, 2020 

import Cell

class Grid:

    def __init__(self, file_path):
        '''
        Constructor for a grid
    
        Parameters:
            file_path: the file location from which the grid will be constructed
        '''
        self.grid = []

        file_ = open(file_path, "r")
        for row_num, line in enumerate(file_):
            # Read line of file into individual integers
            values = list(map(int, line.rstrip()))
            row = []
            for col_num, v in enumerate(values):
                # Create a cell for each value
                row.append(Cell.Cell(row_num, col_num, None if v==0 else v))
            self.grid.append(row)
        
    def Get_Peers(self, cell: Cell):
        '''
        Returns a list of the 20 cells that are peers to the passed cell.
        '''
        peers = []
        # Get elements in same row and column
        peers += [self.grid[cell.row][c] for c in range(9) if c != cell.column]
        peers += [self.grid[r][cell.column] for r in range(9) if r != cell.row]

        # Get peers in same 3x3 but not in same row or column
        box_rows = [r for r in range((cell.row // 3) * 3, (cell.row // 3 + 1) * 3) if r != cell.row]
        box_cols = [c for c in range((cell.column // 3) * 3, (cell.column // 3 + 1) * 3) if c != cell.column]

        peers += [self.grid[r][c] for r in box_rows for c in box_cols]

        return peers

    def Get_3x3(self, cell: Cell):
        '''
        Get the other 8 cells in the same 3x3 grid
        '''
        cells = []
        
        box_rows = [r for r in range((cell.row // 3) * 3, (cell.row // 3 + 1) * 3)]
        box_cols = [c for c in range((cell.column // 3) * 3, (cell.column // 3 + 1) * 3)]

        cells += [self.grid[r][c] for r in box_rows for c in box_cols if r!=cell.row or c!=cell.column]
        return cells
    
    def Get_Row(self, cell: Cell):
        '''
        Get the other 8 cells in the same row
        '''
        return [x for x in self.grid[cell.row] if x is not cell]

    def Get_Column(self, cell: Cell):
        '''
        Get the other 8 cells in the same column
        '''
        return [x for x in self.grid[r][cell.column] for r in range(9) if x is not cell]

    def Get_All(self):
        '''
        Returns a 1-dimensional list of all the cells in the grid, row by row
        '''
        cells = []
        for r in self.grid:
            for c in r:
                cells.append(c)

        return cells

    def __str__(self):
        '''
        Returns a nicely formatted representation of the grid cells
        '''

        output = ""

        for r in range(0, 9):
            for c in range(0, 9):
                val = self.grid[r][c].value
                output += "." if val is None else str(val)
                if c in [2,5]:
                    output += " | "
            if r != 8:
                output += "\n"
            if r in [2,5]:
                output += "----+-----+----\n"
        
        return output

# Provides elements of a Sudoku puzzle to be used in the solving algorithm
# Author:   Blake Freer
# Date:     October 13, 2020

class Cell:
    '''
    Holds data about one cell
    '''

    def __init__(self, row, column, value):
        '''
        Constructor for a cell

        Parameters:
            row:    row number of the cell, 0 based
            column: column number of a cell, 0 based
            value:  the number that this cell holds, or None if the cell is undetermined
        '''
        self.row = row
        self.column = column
        self.value = value
        self._possible_values = set(range(1, 9+1))   # All values that the cell can hold

        if self.value:
            self._possible_values = set([self.value])

    def Eliminate_Option(self, num):
        '''
        Removes a possible value, due to more information becoming available elsewhere.

        Returns:
            True if the cell becomes solved
            False if the cell is still not solved, or there is an error
        '''
        self._possible_values.discard(num)

        if len(self._possible_values) == 1:
            # If all other values have been eliminated, solve the cell
            self.value = list(self._possible_values)[0]
            return True

        if len(self._possible_values) == 0:
            print("Error in solving, no possible value for this cell")

        return False

    def __str__(self):
        return str(self.value)

class Grid:
    '''
    Container for the 9x9 grid of cells, providing methods for retrieving specific cells
    '''

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
                row.append(Cell(row_num, col_num, None if v==0 else v))
            self.grid.append(row)
    
    def Get_3x3(self, cell: Cell):
        '''
        Returns a list of the cells in the 3x3 sub-grid that the passed cell is a part of, excluding the passed cell
        '''
        cells = []

        # Get rows and columns where the 3x3 grid lies
        rows = range((cell.row // 3) * 3, (cell.row // 3 + 1) * 3)
        cols = range((cell.col // 3) * 3, (cell.col // 3 + 1) * 3)

        for r in rows:
            for c in cols:
                cells.append(self.grid[r][c])
        
        cells.remove(cell)
        return cells
    
    def Get_Cross(self, cell: Cell):
        '''
        Returns a list of the cells that share a row or column with the pass cell, excluding the passed cell
        '''
        cells = []
        for r in list(range(0, 9)).remove(cell.row):
            cells.append(self.grid[r][cell.column])
        for c in list(range(0, 9)).remove(cell.column):
            cells.append(self.grid[cell.row][c])

        return cells


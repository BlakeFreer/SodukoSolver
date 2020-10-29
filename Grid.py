# Container for the 9x9 grid of cells, providing methods for retrieving specific cells
# Author:   Blake Freer
# Date:     October 14, 2020 

import Cell

class InputPuzzleError(Exception):
    pass

class Grid:

    def __init__(self, puzzle_string):
        '''
        Constructor for a grid
    
        Parameters:
            puzzle_string: the unsolved puzzle data
        '''
        self.grid = []

        # Remove whitespace from string
        puzzle_string = "".join(puzzle_string.split())
        # Remove | characters and replace . with 0
        puzzle_string = puzzle_string.replace("|", "")
        puzzle_string = puzzle_string.replace(".", "0")

        if len(puzzle_string) != 81:
            raise InputPuzzleError("Puzzle length is not 81")
        if not puzzle_string.isdigit():
            raise InputPuzzleError("Puzzle may only contain digits, whitespace, and the \".\" or \"|\" characters")

        # The number of unsolved cells are the cells that are 0 to start
        self.unsolved_cells = puzzle_string.count("0")

        for i in range(0, 81, 9):
            # Iterate though the 81 characters, 9 digits at a time
            row_nums = [int(x) for x in puzzle_string[i:i+9]]
            new_row = []
            for c, digit in enumerate(row_nums):
                # Create 9 new cells with the current row data
                new_row.append(Cell.Cell(i/9, c, None if digit == 0 else digit))
            # Add the row to the grid
            self.grid.append(new_row)
        
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

    def Get_Box(self, box_num: int):
        '''
        Returns the 9 cells in a 3x3 box. Boxes are numbered 0-8, top to bottom across the rows. ex box 1 = top middle
        '''
        box_rows = range((box_num // 3) * 3, (box_num // 3 + 1) * 3)
        box_cols = range((box_num % 3) * 3, (box_num % 3 + 1) * 3)

        return [self.grid[r][c] for r in box_rows for c in box_cols]
    
    def Get_Row(self, row_num: int):
        '''
        Returns the 9 cells in a row. Rows numbered 0-8, top -> down
        '''
        return self.grid[row_num]

    def Get_Col(self, col_num: int):
        '''
        Returns the 9 cells in a column. Columns numbered 0-8, left-> right
        '''
        return [self.grid[r][col_num] for r in range(9)]

    def __str__(self):
        '''
        Returns a nicely formatted representation of the grid
        '''
        output = ""
        for i, row in enumerate(self.grid):
            for j, c in enumerate(row):
                output += str(c)
                if j in [2,5]:
                    output += "|"
            if i != 8:
                output += "\n"
            if i in [2,5]:
                output += "---+---+---\n"
        
        return output


    # OBSELETE
    def Get_3x3(self, cell: Cell):
        '''
        Get the other 8 cells in the same 3x3 grid
        '''
        
        box_rows = [r for r in range((cell.row // 3) * 3, (cell.row // 3 + 1) * 3)]
        box_cols = [c for c in range((cell.column // 3) * 3, (cell.column // 3 + 1) * 3)]

        cells = [self.grid[r][c] for r in box_rows for c in box_cols if r!=cell.row or c!=cell.column]
        return cells
    
    def Get_Row_Old(self, cell: Cell):
        '''
        Get the other 8 cells in the same row
        '''
        return [x for x in self.grid[cell.row] if x is not cell]

    def Get_Column(self, cell: Cell):
        '''
        Get the other 8 cells in the same column
        '''
        return [self.grid[r][cell.column] for r in range(9) if r != cell.row]

    def Get_All(self):
        '''
        Returns a 1-dimensional list of all the cells in the grid, row by row
        '''
        cells = []
        for r in self.grid:
            for c in r:
                cells.append(c)

        return cells
        
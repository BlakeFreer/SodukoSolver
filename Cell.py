# Holds data about one cell and provides methods for solving the cell
# Author:   Blake Freer
# Date:     October 15, 2020 

import Grid
from string import ascii_uppercase

class Cell:

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
        self.possible_values = set(range(1, 9+1))   # All digit that the cell can hold

        if self.value:
            # If the cell is already solved, then change its possible digits to its value 
            self.possible_values = set([self.value])

    def Remove_Option(self, digit):
        '''
        Remove a digit from the set of possible digits. Return True if the cell becomes solved, False otherwise
        '''
        
        if digit not in self.possible_values:
            # If the digit was already eliminated, do nothing and return that the cell did not become solved
            return False
        
        self.possible_values.remove(digit)

        if len(self.possible_values) == 1:
            # The cell becomes solved if there is only one remaining possible digit
            self.value = self.possible_values.pop()
            self.possible_values = set([self.value])
            return True
        else:
            # If the digit was removed and other options still exist, return False
            return False

    def Solve_By_Peers(self, grid):
        '''
        If this cell is the only cell in its row, column, or 3x3 that can hold a specific value, solve it with that value
        '''

        for s in [grid.Get_Row(self), grid.Get_Column(self), grid.Get_3x3(self)]:
            # Go through row, column and 3x3
            for d in self.possible_values:
                # Check if each possible digit in this cell is not in any of the other cells in the row/column/3x3
                if d not in set().union(*[x.possible_values for x in s]):
                    self.value = d
                    self.possible_values = set([d])
                    return True
        
        return False

    def __str__(self):
        '''
        Returns the Cell formatted as its position (ex. A1) and its value / set of possible digits
        '''
        return "{r}{c}: {val}".format(
            r = ascii_uppercase[self.row],
            c = self.column+1,
            val = str(self.value) if self.value else str(self.possible_values)
        )
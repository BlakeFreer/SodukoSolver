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
        self.possible_digits = set(range(1, 9+1))   # All digit that the cell can hold

        if self.value:
            # If the cell is already solved, then change its possible digits to its value 
            self.possible_digits = {self.value}

    def Eliminate_Digits(self, digits: set):
        '''
        Remove a digit from the set of possible digits. Return True if the cell becomes solved, False otherwise
        '''
        
        difference = self.possible_digits - digits

        if self.value or self.possible_digits == difference:
            # If cell is already solved, or if removing the digits has no effect, the cell doesn't become solved
            return False

        self.possible_digits = difference

        if len(self.possible_digits) == 1:
            # The cell becomes solved if there is only one remaining possible digit
            (self.value,) = self.possible_digits
            return True
        else:
            # If the digit was removed and other options still exist, return False
            return False

    def __str__(self):
        '''
        Returns the Cell formatted as its position (ex. A1) and its value / set of possible digits
        '''
        return "{r}{c}: {val}".format(
            r = ascii_uppercase[self.row],
            c = self.column+1,
            val = str(self.value) if self.value else "."
        )
# Holds data about one cell
# Author:   Blake Freer
# Date:     October 14, 2020 

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
        self._possible_values = set(range(1, 9+1))   # All values that the cell can hold

        if self.value:
            self._possible_values = set([self.value])

    def Eliminate_Option(self, num, grid: Grid):
        '''
        Removes a possible value, due to more information becoming available elsewhere.

        Returns:
            True if the cell becomes solved
            False if the cell is still not solved, or there is an error
        '''
        
        if num not in self._possible_values:
            return False

        self._possible_values.discard(num)

        if len(self._possible_values) == 1:
            # If all other values have been eliminated, solve the cell
            self.value = list(self._possible_values)[0]
            return True

        if len(self._possible_values) == 0:
            raise ValueError("Error in solving, no possible value for this cell")

        return False

    def __str__(self):
        return "{r}{c}: {val}".format(
            r = ascii_uppercase[self.row],
            c = self.column+1,
            val = str(self.value) if self.value else str(self._possible_values)
            )
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
        self.possible_values = set(range(1, 9+1))   # All values that the cell can hold

        if self.value:
            self._possible_values = set([self.value])

    def Remove_Option(self, digit):
        '''
        Remove a digit from the set of possible digits. Return True if the cell becomes solved, False otherwise
        '''
        
        if digit not in self.possible_values or self.value:
            # If the digit was already eliminated, do nothing
            return False
        
        self.possible_values.remove(digit)

        if len(self.possible_values) == 1:
            # The cell becomes solved if there is only one remaining option
            self.value = self.possible_values.pop()
            self.possible_values = set([self.value])
            return True
        else:
            # If the digit was removed and other option still exist, return False
            return False

    def Solve_By_Peers(self, grid):
        '''
        If this cell is the only cell in its row, column, or 3x3 that can hold a specific value, solve it with that value
        '''
        for d in self.possible_values:
            if d not in set().union(*[x.possible_values for x in grid.Get_Row(self)]):
                self.value = d
                self.possible_values = set([d])
                return True

            if d not in set().union(*[x.possible_values for x in grid.Get_Column(self)]):
                self.value = d
                self.possible_values = set([d])
                return True
                
            if d not in set().union(*[x.possible_values for x in grid.Get_3x3(self)]):
                self.value = d
                self.possible_values = set([d])
                return True
        
        return False

    def __str__(self):
        return "{r}{c}: {val}".format(
            r = ascii_uppercase[self.row],
            c = self.column+1,
            val = str(self.value) if self.value else str(self.possible_values)
        )
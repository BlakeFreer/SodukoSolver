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

    def TrySolveCell(self):
        '''
        If the cell only has one possible value, set the cell to that value
        '''
        if len(self._possible_values) == 1:
            self.value = list(self._possible_values)[0]
            return True
        return False

    def Update_Cell(self, grid: Grid):
        '''
        Check the cells in the same 3x3, row and column. If there is a digit that can only be placed in this cell, solve the cell.
        '''
        if self.value:
            # Do nothing if already solved
            return False
        
        if self.TrySolveCell():
            #print("solved {} by clue".format(str(self)))
            return True

        # sets_to_check = [grid.Get_3x3(self), grid.Get_Row(self), grid.Get_Column(self)]
        # for s in sets_to_check:
        #     only_here = self._possible_values - set().union(*[x._possible_values for x in s])
        #     if len(only_here) == 1:
        #         #print("solved {} by peer".format(str(self)))
        #         self._possible_values = only_here
        #         return self.TrySolveCell()

        return False

    def Check_Peers(self, grid):
        cell_sets_to_check = [grid.Get_3x3(self), grid.Get_Row(self), grid.Get_Column(self)]
        for _set in cell_sets_to_check:
            only_here = self._possible_values - set().union(*[x._possible_values for x in _set])
            if len(only_here) == 1:
                self._possible_values = only_here
                self.value = list(self._possible_values)[0]


    def Update(self, grid: Grid, digitToRemove):
        '''
        Use a value in a peer cell to update this cell
        '''
        print("Updating {}".format(self))
        if digitToRemove not in self._possible_values:
            return False
        
        self._possible_values.remove(digitToRemove)
        
        if len(self._possible_values) == 1:
            # If the cell can only have one digit, assign it the the value
            self.value = list(self._possible_values)[0]
        else:
            self.Check_Peers(grid)

        for peer in grid.Get_Peers(self):
            peer.Check_Peers(grid)

        return self.value is not None

    def Eliminate_Option(self, num, grid: Grid):
        '''
        Removes a possible value, due to more information becoming available elsewhere.

        Returns:
            True if the cell becomes solved
            False if the cell is still not solved, or there is an error
        '''

        if num not in self._possible_values:
            return False

        self._possible_values.remove(num)

        return self.Update_Cell(grid)

    def __str__(self):
        return "{r}{c}: {val}".format(
            r = ascii_uppercase[self.row],
            c = self.column+1,
            val = str(self.value) if self.value else str(self._possible_values)
        )
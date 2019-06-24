from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.

        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.

        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.

        :return:Returns the number of columns in the grid. 
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.
        
        :param coord_list: 
        :return: 
        """
        for rows in range(self._grid.num_rows()):
            for cols in range(self._grid.num_cols()):
                self.clear_cell(rows, cols)
        for c in coord_list:
            self.set_cell(c[0], c[1])

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?
        
        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = LifeGrid.DEAD_CELL

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = LifeGrid.LIVE_CELL

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.

        :param row: row of the cell.
        :param col: column of the cell.
        :return: 
        """
        n = 0
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                try:
                    if self.is_live_cell(row+r, col+c) and (r != 0 or c != 0):
                        n += 1
                except AssertionError:
                    pass
        return n

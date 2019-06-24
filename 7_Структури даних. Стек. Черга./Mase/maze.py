# Implements the Maze ADT using a 2-D array.
from arrays import Array2D
from lliststack import Stack

class Maze :
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    # Creates a maze object with all cells marked as open.
    def __init__(self, num_rows, num_cols):
        self._mazeCells = Array2D(num_rows, num_cols)
        self._startCell = None
        self._exitCell = None

    # Returns the number of rows in the maze.
    def num_rows( self ):
        return self._mazeCells.num_rows()

    # Returns the number of columns in the maze.
    def num_cols( self ):
        return self._mazeCells.num_cols()

    # Fills the indicated cell with a "wall" marker.
    def setWall( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

    # Sets the starting cell position.
    def setStart( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._startCell = _CellPosition( row, col )

    # Sets the exit cell position.
    def setExit( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exitCell = _CellPosition( row, col )

    # Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def findPath(self):
        """
        Attempts to solve the maze by finding a path from the starting cell to the exit.
        Returns True if a path is found and False otherwise.
        """
        pos= _CellPosition(self._startCell.row, self._startCell.col)
        self._markPath(pos.row, pos.col)
        while (pos.row, pos.col) != (self._exitCell.row, self._exitCell.col):
            for i in [(pos.row + 1, pos.col), (pos.row - 1, pos.col),
                       (pos.row, pos.col + 1), (pos.row, pos.col - 1)]:
                (a, b) = i
                if self._validMove(a, b):
                    self._markPath(a, b)
                    pos = _CellPosition(a, b)
                    break
            else:
                for i in [(pos.row, pos.col - 1), (pos.row + 1, pos.col),
                          (pos.row, pos.col + 1), (pos.row - 1, pos.col)]:
                    (a, b) = i
                    if self._mazeCells[a, b] == "x":
                        self._markTried(pos.row, pos.col)
                        pos.row, pos.col = a, b
                        break
                else:
                    return False
        else:
            return True

    def reset(self):
        """

        The function resets the maze by removing all "path" and "tried" tokens.
        """
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if self._mazeCells[i, j] in ['x', 'o']:
                    self._mazeCells[i, j] = None

    def draw(self):
        """
        The function Prints a text-based representation of the maze.
        """
        for i in range(self.num_rows()):
            s = str()
            for j in range(self.num_cols()):
                if self._mazeCells[i, j] is None:
                    s += "  "
                else:
                    s += self._mazeCells[i, j] + " "
            print(s)
        print(" ")



    # Returns True if the given cell position is a valid move.
    def _validMove( self, row, col ):
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._mazeCells[row, col] is None

    # Helper method to determine if the exit was found.
    def _exitFound( self, row, col ):
        return row == self._exitCell.row and col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried( self, row, col ):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def _markPath( self, row, col ):
        self._mazeCells[row, col] = self.PATH_TOKEN

# Private storage class for holding a cell position.
class _CellPosition( object ):
    def __init__(self, row, col):
        self.row = row
        self.col = col




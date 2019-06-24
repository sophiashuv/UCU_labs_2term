import ctypes


class Array:
    """
    Creates an array with size elements.
    """
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Array size must be > 0")
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """
        Returns the size of the array.
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the contents of the index element.
        """
        if index < 0 or index > len(self):
            raise IndexError("Array subscript out of range")
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.
        """
        if index < 0 or index > len(self):
            raise IndexError("Array subscript out of range")
        self._elements[index] = value

    def clear(self, value):
        """
        Clears the array by setting each element to the given value.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.
        """
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    """
    An iterator for the Array ADT.
    """

    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration


# Implementation of the Array2D ADT using an array of arrays.

class Array2D:
    """
    Creates a 2 -D array of size numRows x numCols.
    """
    ROW_INDEX = 0
    COL_INDEX = 1

    def __init__(self, num_rows, num_cols):
        """
        Create a 1 -D array to store an array reference for each row.
        """
        self.rows = Array(num_rows)

        for i in range(num_rows):
            self.rows[i] = Array(num_cols)

    # Returns the number of rows in the 2 -D array.
    def num_rows(self):
        """
        The function returns number of rows
        """
        return len(self.rows)

    # Returns the number of columns in the 2 -D array.
    def num_cols(self):
        """
        The function returns number of colums
        """
        return len(self.rows[0])

    # Clears the array by setting every element to the given value.
    def clear(self, value):
        """
        The function clears array
        """
        for row in self.rows:
            row.clear(value)

    # Gets the contents of the element at position [i, j]
    def __getitem__(self, index_tuple):
        """
        The function returns concrete element of array
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols(), \
            "Array subscript out of range."
        array_1d = self.rows[row]
        return array_1d[col]

    # Sets the contents of the element at position [i,j] to value.
    def __setitem__(self, index_tuple, value):
        """
        The function sets an item
        """
        if len(index_tuple) != 2:
            raise IndexError("Invalid number of array subscripts.")
        row = index_tuple[Array2D.ROW_INDEX]
        col = index_tuple[Array2D.COL_INDEX]
        if row < 0 or row > self.num_rows() or col < 0 or col > self.num_cols():
            raise IndexError("Array subscript out of range.")
        array_1d = self.rows[row]
        array_1d[col] = value


class GreyscaleImage:
    """Class for grey image representation"""
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.arrey_2 = Array2D(nrows, ncols)

    def width(self):
        """
        The function returns width of array
        """
        return self.ncols

    def height(self):
        """
        The function returns height of array
        """
        return self.nrows

    def clear(self, value):
        """
        The function clears array
        """
        for i in range(self.nrows):
            for j in range(self.ncols):
                self.arrey_2[i, j] = value

    def __getitem__(self, index_tuple):
        """
        The function returns concrete element of array
        """
        if len(index_tuple) != 2:
            raise ValueError("Invalid number of array subscripts.")
        row = index_tuple[0]
        col = index_tuple[1]
        assert row >= 0 and row < self.height() \
               and col >= 0 and col < self.width(), \
            "Array subscript out of range."
        return self.arrey_2[row, col]

    def __setitem__(self, index_tuple, value):
        """
        The function sets an item
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        if row < 0 or row > self.height() or col < 0 or col > self.width():
            raise IndexError("Array subscript out of range.")
        self.arrey_2[row, col] = value

    def __str__(self):
        """
        The function returns string for array representation
        """
        s = ""
        for i in range(self.nrows):
            for j in range(self.ncols):
                s += '|' + ' '*(3 - len(str(self.arrey_2[i, j]))) + str(self.arrey_2[i, j])
            s += '\n'
        return s

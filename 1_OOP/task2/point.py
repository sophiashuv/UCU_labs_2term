import math
import doctest

class Point():
    ''' Class for point representation '''


    def __init__(self, x, y):
        '''
        (Point, int, int,) -> NoneType
        Create new point
        >>> point1 = Point(1, 1)
        >>> point1.x
        1
        >>> point1.y
        1
        '''
        self.x = x
        self.y = y


    def count_line(self, point):
        '''
        (Pount) -> int
        Return length between two points
        >>> point1 = Point(1, 1)
        >>> point2 = Point(1, 2)
        >>> point1.count_line(point2)
        1.0
        '''
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)


if __name__ == "__main__":
    doctest.testmod()

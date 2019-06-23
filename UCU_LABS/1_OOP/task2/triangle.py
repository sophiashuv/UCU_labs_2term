import point
import math
import doctest

class Triangle():
    ''' Class for triangle representation '''


    def __init__(self, point1, point2, point3):
        '''
        (Triangle, int, int, int) -> NoneType
        Create new triangle
        >>> triangle = Triangle((1,1), (3,1), (2,3))
        >>> triangle.point1
        (1, 1)
        '''
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3


    def is_triangle(self):
        '''
        (Triangle) -> bool
        Returns True whether triangle exist
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.is_triangle()
        True
        '''
        a = self.point1.count_line(self.point2)
        b = self.point1.count_line(self.point3)
        c = self.point2.count_line(self.point3)
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False


    def perimeter(self):
        '''
        (Triangle) -> float
        Return the perimeter of the triangle
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.perimeter()
        6.47213595499958
        '''
        a = self.point1.count_line(self.point2)
        b = self.point1.count_line(self.point3)
        c = self.point2.count_line(self.point3)
        if self.is_triangle():
            return a + b + c
        else:
            return None


    def area(self):
        '''
        (Triangle) -> float
        Return the area of the triangle
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.area()
        2.0
        '''
        a = self.point1.count_line(self.point2)
        b = self.point1.count_line(self.point3)
        c = self.point2.count_line(self.point3)
        if self.is_triangle():
            p = self.perimeter()/2
            return math.sqrt(p*(p-a)*(p-b)*(p-c))
        else:
            return None


if __name__ == "__main__":
    doctest.testmod()
class Point:
    """ Class for Point representation """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_xposition(self):
        """
        The function returns position of x
        """
        return self.x

    def get_yposition(self):
        """
        The function returns position of y
        """
        return self.y

    def __eq__(self, other):
        """
        The function returns True if two points are same
        """
        if type(other) == self.__class__:
            if self.x == other.x and self.y == other.y:
                return True
            return False
        return False


class Line:
    """ Class for line representation """
    def __init__(self, point1, point2):
        """
        Tre function defines two points of a line
        """
        self.point1 = point1
        self.point2 = point2

    def intersect(self, other):
        """
        The function returns the point of two lines intersection
        """
        p1_y = self.point1.get_yposition()
        p2_y = self.point2.get_yposition()
        p1_x = self.point1.get_xposition()
        p2_x = self.point2.get_xposition()

        op1_y = other.point1.get_yposition()
        op2_y = other.point2.get_yposition()
        op1_x = other.point1.get_xposition()
        op2_x = other.point2.get_xposition()

        k1 = (p1_y - p2_y) / (p1_x - p2_x)
        b1 = p1_y - k1*p1_x

        k2 = (op1_y - op2_y) / (op1_x - op2_x)
        b2 = op1_y - k2 * op1_x
        if k1 == k2 and b1 == b2:
            return self
        if k1 == k2:
            return None
        else:
            x = (b2 - b1)/(k1-k2)
            y = k1*x+b1
            return Point(x, y)

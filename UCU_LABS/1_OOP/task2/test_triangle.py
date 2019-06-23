import point
from triangle import Triangle


triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
print(triangle.is_triangle())
print(triangle.perimeter())
print(triangle.area())
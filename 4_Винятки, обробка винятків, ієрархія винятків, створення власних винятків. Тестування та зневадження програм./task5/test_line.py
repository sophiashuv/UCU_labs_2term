import unittest
from line import *


class LineTestcase(unittest.TestCase):
    def setUp(self):
        self.l1 = Line(Point(2, 2), Point(4, 0))
        self.l2 = Line(Point(1, 0), Point(4, 3))
        self.l3 = Line(Point(0, 0), Point(1, 3))
        self.l4 = Line(Point(0, 1), Point(1, 4))
        self.l5 = Line(Point(0, 0), Point(3, 3))
        self.l6 = Line(Point(2, 2), Point(1, 1))

    def test_intersect(self):
        self.assertTrue(isinstance(self.l1.intersect(self.l5), Point))
        self.assertTrue(isinstance(self.l5.intersect(self.l6), Line))
        self.assertEqual(self.l1.intersect(self.l2), Point(2.5, 1.5))
        self.assertEqual(self.l1.intersect(self.l2), Point(2.5, 1.5))

    def test_intersection_none(self):
        self.assertIsNone(self.l3.intersect(self.l4))
        self.assertIsNone(self.l5.intersect(self.l2))

    def test_intersection_one_line(self):
        self.assertEqual(self.l5.intersect(self.l6), self.l5)

    def tearDown(self):
        self.l1 = None
        self.l2 = None
        self.l3 = None
        self.l4 = None
        self.l5 = None
        self.l6 = None


if __name__ == '__main__':
    unittest.main()

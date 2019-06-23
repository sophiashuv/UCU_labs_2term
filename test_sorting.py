import unittest
from is_sorted import is_sorted


class TestIs_sorted(unittest.TestCase):
    def test_is_sorted(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([6, 7]))
        self.assertTrue(is_sorted([101, 109, 150]))
        self.assertTrue(is_sorted([1, 1, 1]))

    def test_is_not_sorted(self):
        self.assertFalse(is_sorted([6, 7, 9, 4, 5]))
        self.assertFalse(is_sorted([]))
        self.assertFalse(is_sorted([7, 21, -3, 0]))

    def test_is_sorted_list(self):
        self.assertFalse(is_sorted("abcd"))
        self.assertFalse(is_sorted("1234"))
        self.assertFalse(is_sorted(1234))
        self.assertFalse(is_sorted({1, 2, 3, 4}))

    def test_is_sorted_list_int(self):
        self.assertFalse(is_sorted(["str", "dfg", "ghj"]))
        self.assertFalse(is_sorted(["1", "2", "3", "4"]))
        self.assertFalse(is_sorted([1.5, 4.6, 9.0]))
        self.assertFalse(is_sorted([[1, 2, 3], [2, 6, 7], [5, 7, 8]]))


if __name__ == '__main__':
    unittest.main()

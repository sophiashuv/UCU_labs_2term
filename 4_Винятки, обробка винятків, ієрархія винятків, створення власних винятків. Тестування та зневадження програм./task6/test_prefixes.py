import unittest
from all_prefixes import all_prefixes


class Testall_prefixes(unittest.TestCase):

    def test_all_prefixes(self):
        self.assertSetEqual(all_prefixes("lead"), {"l", "le", "lea", "lead"})
        self.assertSetEqual(all_prefixes("lalalend"),
                            {'l', 'la', 'lal', 'lala', 'lalal', 'lalale', 'lalalen', 'lalalend'})
        self.assertSetEqual(all_prefixes("eeeeeee"), {'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee'})

    def test_all_prefixes_string(self):
        self.assertIsNone(all_prefixes(123))
        self.assertIsNone(all_prefixes([1, 2, 3]))
        self.assertIsNone(all_prefixes(["Hello"]))

    def test_all_prefixes_null(self):
        self.assertSetEqual(all_prefixes(" "), {' '})
        self.assertIsNone(all_prefixes(0))
        self.assertIsNone(all_prefixes([]))

    def test_all_prefixes_in(self):
        self.assertNotIn("m", all_prefixes("lead"))
        self.assertNotIn("deal", all_prefixes("lead"))
        self.assertNotIn(" ", all_prefixes("lead"))


if __name__ == '__main__':
    unittest.main()

import unittest
from chess import *


class TestChessMethods(unittest.TestCase):
    def test_knight(self):
        self.assertTrue(n_allowed((5,5), (7,4)))
        self.assertTrue(n_allowed((5,5), (7,6)))
        self.assertTrue(n_allowed((5,5), (6,7)))
        self.assertTrue(n_allowed((5,5), (4,7)))
        self.assertTrue(n_allowed((5,5), (3,4)))
        self.assertTrue(n_allowed((5,5), (3,6)))
        self.assertTrue(n_allowed((5,5), (4,7)))
        self.assertTrue(n_allowed((5,5), (6,7)))

        self.assertFalse(n_allowed((6,6), (4,4)))
        self.assertFalse(n_allowed((5,5), (4,4)))
        self.assertFalse(n_allowed((5,5), (5,7)))
        self.assertFalse(n_allowed((5,5), (7,5)))
        self.assertFalse(n_allowed((5,5), (3,5)))
        self.assertFalse(n_allowed((5,5), (4,5)))
        self.assertFalse(n_allowed((5,5), (8,3)))
        self.assertFalse(n_allowed((5,5), (8,4)))


    def test_out_of_bounds(self):
        self.assertFalse(n_allowed((1, 1), (-1, 2)))
        self.assertFalse(n_allowed((2, 2), (0, 1)))
        self.assertFalse(n_allowed((6, 7), (7, 9)))
        self.assertFalse(n_allowed((7, 7), (9, 8)))

        self.assertFalse(n_allowed((-1, 2),(1, 1)))
        self.assertFalse(n_allowed((0, 1),(2,2)))
        self.assertFalse(n_allowed((7, 9),(6,7)))
        self.assertFalse(n_allowed((9, 8),(7,7)))


if __name__ == '__main__':
    unittest.main()

import unittest
from chess import *


class TestChessMethods(unittest.TestCase):
    def test_bishop(self):
        self.assertTrue(b_allowed((3,3), (6,6)))
        self.assertTrue(b_allowed((2,2), (5,5)))
        self.assertTrue(b_allowed((8,8), (6,6)))
        self.assertTrue(b_allowed((6,6), (8,8)))
        self.assertTrue(b_allowed((6,6), (8,4)))
        self.assertTrue(b_allowed((6,6), (4,4)))
        self.assertTrue(b_allowed((6,6), (4,8)))

        self.assertFalse(b_allowed((1,2), (2,2)))
        self.assertFalse(b_allowed((1,2), (1,4)))
        self.assertFalse(b_allowed((6,6), (7,8)))

    def test_out_of_bounds(self):
        self.assertFalse(b_allowed((2, 2), (0, 0)))
        self.assertFalse(b_allowed((2, 2), (4, 0)))
        self.assertFalse(b_allowed((6, 6), (9, 9)))
        self.assertFalse(b_allowed((1, 1), (0, 0)))
        self.assertFalse(b_allowed((2, 2), (0, 0)))
        self.assertFalse(b_allowed((7, 2), (9, 0)))


if __name__ == '__main__':
    unittest.main()

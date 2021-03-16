import unittest
from chess import *


class TestChessMethods(unittest.TestCase):
    def test_rook(self):
        self.assertTrue(r_allowed((3,3), (4,3)))
        self.assertTrue(r_allowed((3,3), (5,3)))
        self.assertTrue(r_allowed((3,3), (1,3)))
        self.assertTrue(r_allowed((3,3), (3,1)))
        self.assertTrue(r_allowed((3,3), (3,2)))
        self.assertTrue(r_allowed((3,3), (3,4)))
        self.assertTrue(r_allowed((3,3), (3,5)))
        self.assertTrue(r_allowed((3,3), (3,8)))

        self.assertFalse(r_allowed((3,3), (3,3)))
        self.assertFalse(r_allowed((3,3), (4,4)))
        self.assertFalse(r_allowed((3,3), (5,5)))
        self.assertFalse(r_allowed((3,3), (1,1)))


    def test_out_of_bounds(self):
        self.assertFalse(r_allowed((1, 1), (1, 0)))
        self.assertFalse(r_allowed((4, 1), (4, 0)))
        self.assertFalse(r_allowed((8, 9), (9, 9)))
        self.assertFalse(r_allowed((1, 1), (0, 1)))
        self.assertFalse(r_allowed((1, 2), (1, 0)))
        self.assertFalse(r_allowed((9, 1), (8, 1)))


if __name__ == '__main__':
    unittest.main()

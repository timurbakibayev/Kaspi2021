import unittest
from chess import *


class TestChessMethods(unittest.TestCase):
    def test_king(self):
        self.assertTrue(k_allowed((3,3), (4,4)))
        self.assertTrue(k_allowed((3,3), (4,3)))
        self.assertTrue(k_allowed((3,3), (4,2)))
        self.assertTrue(k_allowed((3,3), (3,2)))
        self.assertTrue(k_allowed((3,3), (2,2)))
        self.assertTrue(k_allowed((3,3), (2,3)))
        self.assertTrue(k_allowed((3,3), (2,4)))
        self.assertTrue(k_allowed((3,3), (3,4)))

        self.assertFalse(k_allowed((3,3), (3,3)))


    def test_out_of_bounds(self):
        self.assertFalse(k_allowed((1, 1), (0, 0)))
        self.assertFalse(k_allowed((4, 1), (4, 0)))
        self.assertFalse(k_allowed((8, 8), (9, 9)))
        self.assertFalse(k_allowed((1, 1), (0, 0)))
        self.assertFalse(k_allowed((1, 2), (0, 2)))
        self.assertFalse(k_allowed((8, 1), (9, 1)))


if __name__ == '__main__':
    unittest.main()

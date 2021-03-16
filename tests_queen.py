import unittest
from chess import *


class TestChessMethods(unittest.TestCase):
    def test_king(self):  # all king's moves allowed, too
        self.assertTrue(q_allowed((3,3), (4,4)))
        self.assertTrue(q_allowed((3,3), (4,3)))
        self.assertTrue(q_allowed((3,3), (4,2)))
        self.assertTrue(q_allowed((3,3), (3,2)))
        self.assertTrue(q_allowed((3,3), (2,2)))
        self.assertTrue(q_allowed((3,3), (2,3)))
        self.assertTrue(q_allowed((3,3), (2,4)))
        self.assertTrue(q_allowed((3,3), (3,4)))

        self.assertFalse(q_allowed((3,3), (3,3)))

    def test_bishop(self):  # all bishop's moves allowed, too
        self.assertTrue(q_allowed((3,3), (6,6)))
        self.assertTrue(q_allowed((2,2), (5,5)))
        self.assertTrue(q_allowed((8,8), (6,6)))
        self.assertTrue(q_allowed((6,6), (8,8)))
        self.assertTrue(q_allowed((6,6), (8,4)))
        self.assertTrue(q_allowed((6,6), (4,4)))
        self.assertTrue(q_allowed((6,6), (4,8)))

    def test_rook(self):  # all rook's moves allowed, too
        self.assertTrue(q_allowed((3,3), (4,3)))
        self.assertTrue(q_allowed((3,3), (5,3)))
        self.assertTrue(q_allowed((3,3), (1,3)))
        self.assertTrue(q_allowed((3,3), (3,1)))
        self.assertTrue(q_allowed((3,3), (3,2)))
        self.assertTrue(q_allowed((3,3), (3,4)))
        self.assertTrue(q_allowed((3,3), (3,5)))
        self.assertTrue(q_allowed((3,3), (3,8)))


    def test_knight(self):  # all kingt's moves are forbidden!
        self.assertFalse(q_allowed((5,5), (7,4)))
        self.assertFalse(q_allowed((5,5), (7,6)))
        self.assertFalse(q_allowed((5,5), (6,7)))
        self.assertFalse(q_allowed((5,5), (4,7)))
        self.assertFalse(q_allowed((5,5), (3,4)))
        self.assertFalse(q_allowed((5,5), (3,6)))
        self.assertFalse(q_allowed((5,5), (4,7)))
        self.assertFalse(q_allowed((5,5), (6,7)))


    def test_out_of_bounds(self):
        self.assertFalse(q_allowed((1, 1), (0, 0)))
        self.assertFalse(q_allowed((4, 1), (4, 0)))
        self.assertFalse(q_allowed((8, 8), (9, 9)))
        self.assertFalse(q_allowed((9, 9), (8, 8)))
        self.assertFalse(q_allowed((1, 1), (0, 0)))
        self.assertFalse(q_allowed((1, 2), (0, 2)))
        self.assertFalse(q_allowed((8, 1), (9, 1)))
        self.assertFalse(q_allowed((3, 3), (-2, -2)))
        self.assertFalse(q_allowed((-2, -2), (3, 3)))


if __name__ == '__main__':
    unittest.main()

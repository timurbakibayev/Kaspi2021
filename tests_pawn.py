import unittest
from chess import *


class TestChessMethods(unittest.TestCase):
    def test_p(self):
        self.assertTrue(p_allowed((1,2), (1,3), True))
        self.assertFalse(p_allowed((1,2), (1,3), False))

    def test_first_two_cells_true(self):
        self.assertTrue(p_allowed((2,2), (2,4), True))
        self.assertTrue(p_allowed((3,2), (3,4), True))
        self.assertTrue(p_allowed((2,7), (2,5), False))
        self.assertTrue(p_allowed((5,7), (5,5), False))

    def test_first_two_cells_false(self):
        self.assertFalse(p_allowed((2,2), (2,4), False))
        self.assertFalse(p_allowed((3,2), (3,4), False))
        self.assertFalse(p_allowed((2,7), (2,5), True))
        self.assertFalse(p_allowed((5,7), (5,5), True))

    def test_out_of_bounds(self):
        self.assertFalse(p_allowed((2, 1), (2, 2), True))  # White cannot be at y=1
        self.assertFalse(p_allowed((2, 8), (2, 7), False))  # Black cannot be at y=1
        self.assertFalse(p_allowed((2, 8), (2, 9), True))
        self.assertFalse(p_allowed((2, 1), (2, 0), False))
        self.assertFalse(p_allowed((0, 4), (0, 5), True))
        self.assertFalse(p_allowed((0, 5), (0, 4), False))
        self.assertFalse(p_allowed((9, 4), (9, 5), True))
        self.assertFalse(p_allowed((9, 5), (9, 4), False))


if __name__ == '__main__':
    unittest.main()

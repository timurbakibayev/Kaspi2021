import unittest
from chess import *


class TestChessMethods(unittest.TestCase):
    def test_complex_ok(self):
        #  Timur Bakibayev
        board = [
            ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "  "],
            ["BP", "BP", "BP", "  ", "BP", "BP", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "BP", "  "],
            ["  ", "  ", "  ", "BP", "  ", "  ", "  ", "BR"],
            ["  ", "  ", "  ", "WP", "WP", "  ", "WP", "BP"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["WP", "WP", "WP", "  ", "  ", "WP", "  ", "WP"],
            ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"],
        ]

        self.assertTrue(board_move_ok((1,2), (1,4), board))  # WP
        self.assertTrue(board_move_ok((1,2), (1,3), board))
        self.assertTrue(board_move_ok((5,4), (4,5), board))  # EAT

        self.assertFalse(board_move_ok((1,2), (2,2), board))
        self.assertFalse(board_move_ok((1,2), (2,3), board))

        self.assertFalse(board_move_ok((3,1), (2,2), board))
        self.assertFalse(board_move_ok((3,1), (1,3), board))

        # Write your own tests and share with us!


if __name__ == '__main__':
    unittest.main()

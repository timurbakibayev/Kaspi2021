import unittest
from move_on_board import *


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
        # Azamat

        self.assertTrue(board_move_ok((3, 8), (7, 4), board))  # EAT
        self.assertTrue(board_move_ok((6, 7), (6, 5), board))  # BP
        self.assertTrue(board_move_ok((4, 5), (5, 4), board))  # EAT
        self.assertFalse(board_move_ok((4, 4), (4, 5), board))  # WP
        self.assertFalse(board_move_ok((8, 1), (8, 4), board))  # WR
        self.assertFalse(board_move_ok((4, 1), (8, 5), board))  # WQ

        # Nurken

        self.assertTrue(board_move_ok((2, 1), (3, 3), board))  # First WN
        self.assertTrue(board_move_ok((2, 1), (1, 3), board))  # First WN second way of movement
        self.assertTrue(board_move_ok((3, 1), (4, 2), board))  # WB
        self.assertTrue(board_move_ok((3, 1), (5, 3), board))  # WB
        self.assertTrue(board_move_ok((3, 1), (6, 4), board))  # WB
        self.assertTrue(board_move_ok((3, 1), (7, 5), board))  # WB
        self.assertTrue(board_move_ok((3, 1), (8, 6), board))  # WB
        self.assertTrue(board_move_ok((7, 4), (8, 5), board))  # WP eats BP

        self.assertFalse(board_move_ok((2, 1), (2, 2), board))  # WN
        self.assertFalse(board_move_ok((4, 4), (4, 5), board))  # WP can not eat like that
        self.assertFalse(board_move_ok((8, 2), (8, 4), board))  # WP can not eat like that
        self.assertFalse(board_move_ok((5, 1), (6, 2), board))  # WK can not eat WP


    def test_complex_second(self):
        #  Alisher Kuanyshbekov
        board = [
            ["BR", "  ", "  ", "  ", "BK", "BB", "BN", "BR"],
            ["BP", "BP", "BP", "  ", "  ", "BP", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "BP", "  ", "  ", "BP", "  "],
            ["  ", "WR", "  ", "WP", "WP", "  ", "WP", "BP"],
            ["WB", "  ", "BN", "WQ", "  ", "  ", "  ", "WN"],
            ["WP", "  ", "WP", "  ", "  ", "WP", "WB", "  "],
            ["  ", "  ", "  ", "  ", "WK", "  ", "  ", "WR"],
        ]

        self.assertFalse(board_move_ok((1, 2), (1, 3), board))
        self.assertTrue(board_move_ok((5, 4), (4, 5), board))  # EAT P
        self.assertTrue(board_move_ok((8, 3), (7, 5), board))  # EAT N
        self.assertTrue(board_move_ok((2, 4), (2, 7), board))  # EAT R

        self.assertTrue(board_move_ok((5, 8), (3, 8), board))  # long castling
        self.assertTrue(board_move_ok((5, 1), (7, 1), board))  # short castling

        self.assertFalse(board_move_ok((8, 3), (9, 5), board))  # out of board (>8)
        self.assertFalse(board_move_ok((1, 3), (0, 2), board))  # out of board (<1)

        self.assertFalse(board_move_ok((3, 2), (1, 4), board))  # Barrier P
        self.assertFalse(board_move_ok((7, 2), (3, 6), board))  # Barrier B
        self.assertFalse(board_move_ok((8, 8), (4, 8), board))  # Barrier R hor.
        self.assertFalse(board_move_ok((8, 8), (8, 3), board))  # Barrier R vert.
        self.assertFalse(board_move_ok((4, 3), (4, 5), board))  # Barrier Q

        self.assertFalse(board_move_ok((5, 1), (3, 1), board))  # Wrong castling (No rock)
        self.assertFalse(board_move_ok((5, 8), (7, 8), board))  # Wrong castling (Barrier)

        self.assertFalse(board_move_ok((7, 6), (8, 5), board))  # Eat one-colored figure
        self.assertFalse(board_move_ok((5, 1), (6, 2), board))  # Eat one-colored figure

    def test_complex_third(self):
        #  Alisher Kuanyshbekov
        board = [
            ["BR", "  ", "  ", "  ", "BK", "BB", "BN", "  "],
            ["BP", "BP", "BP", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "BP", "  ", "  ", "WP", "  "],
            ["BQ", "WR", "  ", "WP", "  ", "WQ", "WB", "BP"],
            ["WB", "  ", "BN", "  ", "  ", "  ", "  ", "WN"],
            ["WP", "  ", "WP", "  ", "BP", "WP", "  ", "  "],
            ["  ", "  ", "WK", "WR", "  ", "  ", "  ", "  "],
        ]
        self.assertTrue(board_move_ok((5, 2), (5, 1), board))  # P in y=1
        self.assertTrue(board_move_ok((3, 3), (4, 1), board))  # Eat N
        self.assertTrue(board_move_ok((3, 7), (3, 5), board))  # Two steps forward
        # self.assertTrue(board_move_ok((7, 5), (6, 6), board))  # En passant

        self.assertFalse(board_move_ok((5, 8), (3, 8), board))  # Wrong castling (in check)
        self.assertFalse(board_move_ok((1, 4), (3, 5), board))  # Queen move as knight
        # self.assertFalse(board_move_ok((8, 4), (7, 3), board))  # En passant (Not P)


        def test_complex_ok(self):
            # Maira Moldimanova
            board = [
                ["BR", "  ", "BB", "BQ", "BK", "  ", "BN", "BR"],
                ["BP", "BP", "  ", "  ", "  ", "BP", "BP", "  "],
                ["  ", "  ", "BN", "  ", "BP", "  ", "  ", "BP"],
                ["  ", "  ", "  ", "BP", "WP", "  ", "  ", "  "],
                ["  ", "BB", "  ", "WP", "  ", "  ", "  ", "  "],
                ["  ", "  ", "WN", "  ", "  ", "WN", "  ", "  "],
                ["WP", "WP", "  ", "  ", "  ", "WP", "WP", "WP"],
                ["WR", "  ", "WB", "WQ", "WK", "WB", "  ", "WR"],
            ]
            self.assertTrue(board_move_ok((1, 2), (1, 4), board))  # WP
            self.assertTrue(board_move_ok((1, 2), (1, 3), board))

            self.assertTrue(board_move_ok((3,6), (4,4), board))  # EAT
            self.assertTrue(board_move_ok((2, 4), (3, 3), board))
            self.assertTrue(board_move_ok((3, 3), (4, 5), board))

            self.assertFalse(board_move_ok((2, 2), (3, 3), board))
            self.assertFalse(board_move_ok((6, 3), (4, 4), board))

            self.assertFalse(board_move_ok((4, 1), (4, 4), board))
            self.assertFalse(board_move_ok((8,1), (8,6), board))


        def test_bishop_over_figure(self):
            # Timur
            board = [
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "BK", "  "],
                ["  ", "  ", "  ", "BP", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "WB", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "WP", "  ", "  "],
                ["  ", "  ", "BR", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ]

            self.assertFalse(board_move_ok((5, 4), (2, 1), board))
            self.assertFalse(board_move_ok((5, 4), (3, 6), board))
            self.assertFalse(board_move_ok((5, 4), (8, 7), board))
            self.assertFalse(board_move_ok((5, 4), (8, 8), board))


        def test_queen_over_figure(self):
            # Timur
            board = [
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "WP", "  ", "BK", "  "],
                ["  ", "  ", "  ", "BP", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "WQ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "WP", "  ", "  "],
                ["  ", "  ", "BR", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ]

            self.assertFalse(board_move_ok((5, 4), (2, 1), board))
            self.assertFalse(board_move_ok((5, 4), (3, 6), board))
            self.assertFalse(board_move_ok((5, 4), (8, 7), board))
            self.assertFalse(board_move_ok((5, 4), (8, 8), board))
            self.assertFalse(board_move_ok((5, 4), (5, 7), board))


        def test_queen_eats_figure(self):
            # Timur
            board = [
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "WP", "  ", "BK", "  "],
                ["  ", "  ", "  ", "BP", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "WQ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "WP", "  ", "  "],
                ["  ", "  ", "BR", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ]

            self.assertTrue(board_move_ok((5, 4), (3, 2), board))
            self.assertTrue(board_move_ok((5, 4), (4, 5), board))
            self.assertTrue(board_move_ok((5, 4), (7, 6), board))
            self.assertFalse(board_move_ok((5, 4), (5, 6), board))
            self.assertFalse(board_move_ok((5, 4), (6, 3), board))


if __name__ == '__main__':
    unittest.main()

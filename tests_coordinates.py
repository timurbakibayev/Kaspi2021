import unittest
from move_on_board import *


class TestChessMethods(unittest.TestCase):
    def test_coord(self):
        self.assertEqual(coord((1,1)), (7,0))
        self.assertEqual(coord((8,1)), (7,7))
        self.assertEqual(coord((8,8)), (0,7))
        self.assertEqual(coord((1,8)), (0,0))
        self.assertEqual(coord((3,3)), (5,2))


    def test_uncoord(self):
        self.assertEqual(uncoord((7,0)), (1,1))
        self.assertEqual(uncoord((7,7)), (8,1))
        self.assertEqual(uncoord((0,7)), (8,8))
        self.assertEqual(uncoord((0,0)), (1,8))
        self.assertEqual(uncoord((5,2)), (3,3))


    def test_middle(self):
        self.assertEqual(middle((3, 3), (4, 3)), [])
        self.assertEqual(middle((3, 3), (5, 3)), [(4,3)])
        self.assertEqual(middle((3, 3), (7, 3)), [(4,3),(5,3),(6,3)])
        self.assertEqual(middle((3, 3), (1, 3)), [(2,3)])
        self.assertEqual(middle((3, 3), (0, 3)), [(2,3),(1,3)])
        self.assertEqual(middle((3, 3), (7, 7)), [(4,4),(5,5),(6,6)])
        self.assertEqual(middle((3, 3), (5, 1)), [(4,2)])


if __name__ == '__main__':
    unittest.main()

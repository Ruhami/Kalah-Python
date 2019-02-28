from kalah import Kalah
import unittest


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalah(6, 4)

    def test_initial_status(self):
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_illegal_hole(self):
        self.assertRaises(IndexError, self.game.play, -1)
        self.assertRaises(IndexError, self.game.play, 15)

    def test_simple_move(self):
        self.game.play(0)
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_crossing_move(self):
        self.game.play(4)
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 0, 5, 1, 5, 5, 4, 4, 4, 4, 0))

    def test_two_simple_moves(self):
        self.game.play(0)
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))
        self.game.play(8)
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 0, 5, 5, 5, 5, 0))

    def test_player_two_crosses(self):
        self.game.play(0)
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))
        self.game.play(8)
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 0, 5, 5, 5, 5, 0))
        self.game.play(2)
        self.assertEqual(self.game.status(), (0, 5, 0, 6, 6, 5, 1, 5, 0, 5, 5, 5, 5, 0))
        self.game.play(10)
        self.assertEqual(self.game.status(), (1, 6, 0, 6, 6, 5, 1, 5, 0, 5, 0, 6, 6, 1))

    def test_crossing_other_bank(self):
        self.game.set_status([1, 6, 0, 6, 2, 9, 1, 5, 0, 5, 0, 6, 6, 1])
        self.game.play(5)
        self.assertEqual(self.game.status(), (2, 7, 0, 6, 2, 0, 2, 6, 1, 6, 1, 7, 7, 1))

    def test_empty_hole(self):
        self.game.set_status([2, 7, 0, 6, 2, 0, 2, 6, 1, 6, 1, 7, 7, 1])
        self.assertRaises(ValueError, self.game.play, 2)

    def test_bonus_move_player_one(self):
        self.assertEqual(self.game.play(2), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0))

    def test_bonus_move_player_two(self):
        self.game.set_player(1)
        self.assertEqual(self.game.play(9), "Player 2 plays next")

    def test_capture_player_one(self):
        self.game.set_status([2, 7, 0, 6, 2, 0, 2, 6, 1, 6, 1, 7, 7, 1])
        self.game.play(0)
        self.assertEqual(self.game.status(), (0, 8, 0, 6, 2, 0, 4, 6, 1, 6, 0, 7, 7, 1))

    def test_capture_player_two(self):
        self.game.set_player(1)
        self.game.set_status([0, 7, 1, 6, 2, 0, 4, 5, 2, 6, 0, 7, 7, 1])
        self.game.play(8)
        self.assertEqual(self.game.status(), (0, 7, 0, 6, 2, 0, 4, 5, 0, 7, 0, 7, 7, 3))

    def test_non_capture(self):
        self.game.set_player(1)
        self.game.set_status([0, 8, 0, 6, 2, 0, 4, 5, 2, 6, 0, 7, 7, 1])
        self.game.play(8)
        self.assertEqual(self.game.status(), (0, 8, 0, 6, 2, 0, 4, 5, 0, 7, 1, 7, 7, 1))

    def test_end_game(self):
        self.game.set_status([0, 0, 0, 0, 0, 0, 25, 4, 2, 6, 0, 7, 3, 1])
        self.assertEqual(self.game.play(5), "Player 1 wins.")

        self.game.set_status([2, 2, 6, 0, 7, 3, 3, 0, 0, 0, 0, 0, 0, 25])
        self.game.set_player(1)
        self.assertEqual(self.game.play(8), "Player 2 wins.")

        self.game.set_status([0, 0, 0, 0, 0, 0, 24, 3, 2, 6, 0, 7, 4, 2])
        self.assertEqual(self.game.play(5), "Tie")

    def test_4_holes_4_seeds(self):
        print(self.game.render())
        self.game = Kalah(4, 4)
        self.game.set_status([0, 0, 0, 0, 17, 4, 2, 6, 2, 1])
        self.assertEqual(self.game.play(2), "Player 1 wins.")

        self.game.set_status([1, 2, 6, 2, 4, 0, 0, 0, 0, 17])
        self.game.set_player(1)
        self.assertEqual(self.game.play(8), "Player 2 wins.")

        self.game.set_status([0, 0, 0, 0, 16, 3, 2, 6, 3, 2])
        self.assertEqual(self.game.play(2), "Tie")

    def test_rep(self):
        assert repr(Kalah(6, 4)) == "Kalah(4, 6, status=(4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0), player=0)"

    def test_render(self):
        #self.game = Kalah(6, 6)
        x = """	P L A Y E R  2
 ____________________________________________________________
|★★★★  ____    ____    ____    ____    ____    ____    ★★★★|
|★   ★ [_4__] 	[_4__] 	[_4__] 	[_4__] 	[_4__] 	[_4__] 	★   ★|
|★ 0 ★  ____    ____    ____    ____    ____    ____   ★ 0 ★| 
|★★★★	[_4__]	[_4__]	[_4__]	[_4__]	[_4__]	[_4__]	★★★★|
 ____________________________________________________________
	P L A Y E R  1"""
        self.assertEqual(self.game.render(), x)




if __name__ == '__main__':
    unittest.main()

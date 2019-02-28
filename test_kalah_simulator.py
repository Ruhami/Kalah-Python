import unittest
from venv import logger

import kalah_simulator as k_s


class KalahSimulatorTestCase(unittest.TestCase):
    def test_simulation1(self):
        with open(f"data/game_2.txt") as f:
            lines = f.read().splitlines()
        steps = k_s.parse_game(lines)
        for message, status in k_s.simulate_game(6, 6, steps[0]):
            logger.debug(message, status)
        self.assertEqual((0, 0, 0, 0, 0, 0, 38, 0, 0, 0, 0, 0, 0, 34), status)
        self.assertEqual(message, "Player 1 wins.")

    def test_simulation2(self):
        with open(f"data/game_3.txt") as f:
            lines = f.read().splitlines()
        steps = k_s.parse_game(lines)
        for message, status in k_s.simulate_game(6, 6, steps[0]):
            logger.debug(message, status)

        self.assertEqual((0, 0, 0, 0, 0, 0, 47, 0, 0, 0, 0, 0, 0, 25), status)
        self.assertEqual(message, "Player 1 wins.")


if __name__ == '__main__':
    unittest.main()

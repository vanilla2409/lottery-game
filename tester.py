import unittest
from unittest.mock import patch
import random
import builtins

import lottery_game as lg

class TestLotteryGame(unittest.TestCase):

    def test_three_prize_output(self):
        with patch('random.choice') as mock_choice:
            mock_choice.return_value = "Novelty mug - A funny or motivational mug to lift your spirits."
            result = lg.three_prize()
            self.assertEqual(result, "Novelty mug - A funny or motivational mug to lift your spirits.")

    def test_standard_prize_output(self):
        with patch('random.choice') as mock_choice:
            mock_choice.return_value = "E-bike or electric scooter - Perfect for eco-friendly and fun commuting."
            result = lg.standard_prize()
            self.assertEqual(result, "E-bike or electric scooter - Perfect for eco-friendly and fun commuting.")

    def test_four_star_prize_index_bounds(self):
        # Check if it handles index properly and returns one of the valid prizes
        prize = lg.four_star_prize(0)
        self.assertIn(prize, [
            "High-quality suitcase - Durable and stylish, perfect for travel enthusiasts.",
            "Mixer-grinder - A versatile kitchen appliance for cooking convenience.",
            "Air fryer - A trendy gadget for health-conscious food lovers.",
            "Premium coffee maker - Brew barista-quality coffee at home.",
            "Smartwatch - Tracks fitness, notifications, and more.",
            "Portable vacuum cleaner - Compact and efficient for easy cleaning.",
            "Premium cookware set - Includes non-stick pans, pots, and utensils.",
            "Noise-canceling headphones - High-quality sound and comfort.",
            "Kindle e-reader - Perfect for book lovers who want to carry an entire library.",
            "Electric kettle with temperature control - Ideal for tea and coffee enthusiasts."
        ])

    @patch('builtins.print')
    def test_pull_win_five_star(self, mock_print):
        # User is on the 5-star prize index
        x = 5
        five_star = 5
        four_star = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        desired_fs = "Electric luxury car"
        with patch('random.randint', return_value=1):
            new_x, new_five_star = lg.pull(x, four_star, five_star, desired_fs)
            self.assertEqual(new_x, 0)
            self.assertTrue(1 <= new_five_star <= 100)
            mock_print.assert_any_call("You Have Won:", desired_fs)

    @patch('builtins.print')
    def test_pull_four_star(self, mock_print):
        # User hits a four-star prize index
        x = 20
        five_star = 50
        four_star = [10, 20, 30, 40, 60, 70, 80, 90, 100, 110]
        desired_fs = "Cruise"
        new_x, _ = lg.pull(x, four_star, five_star, desired_fs)
        self.assertEqual(new_x, 21)
        mock_print.assert_any_call("\nHURRAY!")

    @patch('builtins.print')
    def test_pull_three_star(self, mock_print):
        # User hits none
        x = 3
        five_star = 80
        four_star = [10, 20, 30, 40, 60, 70, 90, 100, 110, 120]
        desired_fs = "Paris"
        new_x, _ = lg.pull(x, four_star, five_star, desired_fs)
        self.assertEqual(new_x, 4)
        mock_print.assert_any_call("You get:", unittest.mock.ANY)


if __name__ == '__main__':
    unittest.main()

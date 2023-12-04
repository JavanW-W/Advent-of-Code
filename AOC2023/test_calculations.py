import json
import os
import sys
import unittest

from pathlib import Path

import calculations

# Add the project directory to sys.path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))

dir_path = os.path.dirname(os.path.realpath(__file__))

class TestCalculations(unittest.TestCase):
    fixtures = ["test_db.json"]

    def setUp(self):
        """Initialization before tests."""
        with open(os.path.join(dir_path, "test_data.json")) as f:
            self.testData = json.load(f)

    def test_day1_part1(self):
        """Day 1 Part 1 Test Case."""
        data = self.testData["day-1"]
        # test find_calibrations
        total_cal = sum(calculations.find_calibrations(data["part1_input"]))
        self.assertEqual(total_cal, data["part1_solution"])

    def test_day1_part2(self):
        """Day 1 Part 2 Test Case."""
        data = self.testData["day-1"]
        # test find_calibrations_with_strings
        total_cal = \
            sum(calculations.find_calibrations_with_strings(data["part2_input"]))
        self.assertEqual(total_cal, data["part2_solution"])

    def test_day2_part1(self):
        """Day 2 Part 1 Test Case."""
        data = self.testData["day-2"]
        # test find_possible_games
        game_sum = sum(calculations.find_possible_games(data["test_input"], 12, 13, 14))
        self.assertEqual(game_sum, data["part1_solution"])

    def test_day2_part2(self):
        """Day 2 Part 2 Test Case."""
        data = self.testData["day-2"]
        # test minimum cubes power
        power_sum = sum(calculations.find_minimum_cubes_power(data["test_input"]))
        self.assertEqual(power_sum, data["part2_solution"])

    # def test_day3_part1(self):
    #     """Day 3 Part 1 Test Case."""
    #     data = self.testData["day-3"]
    #     # test find_part_numbers
    #     part_number_sum = sum(calculations.find_part_numbers(data["part1_input"]))
    #     self.assertEqual(part_number_sum, data["part1_solution"])

    def test_day4_part1(self):
        """Day 4 Part 1 Test Case."""
        data = self.testData["day-4"]
        # test find_card_scores
        card_score = sum(calculations.find_card_scores(data["test_input"]))
        self.assertEqual(card_score, data["part1_solution"])
    
    def test_day4_part2(self):
        """Day 4 Part 2 Test Case."""
        data = self.testData["day-4"]
        # test find_total_copies
        total_copies = sum(calculations.find_total_copies(data["test_input"]))
        self.assertEqual(total_copies, data["part2_solution"])

if __name__ == '__main__':
    unittest.main()


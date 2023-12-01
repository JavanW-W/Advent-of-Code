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
        # test convert_text_to_digit
        total_cal = sum(calculations.find_calibrations_with_strings(data["part2_input"]))
        self.assertEqual(total_cal, data["part2_solution"])

if __name__ == '__main__':
    unittest.main()


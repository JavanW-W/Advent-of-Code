import json
import os
import sys
import unittest

from math import prod, lcm
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

    def test_day3_part1(self):
        """Day 3 Part 1 Test Case."""
        data = self.testData["day-3"]
        # test find_part_numbers
        part_number_sum = sum(calculations.find_part_numbers(data["test_input"]))
        self.assertEqual(part_number_sum, data["part1_solution"])

    def test_day3_part2(self):
        """Day 3 Part 2 Test Case."""
        data = self.testData["day-3"]
        # test find_part_numbers
        part_number_sum = sum(calculations.find_gear_ratios(data["test_input"]))
        self.assertEqual(part_number_sum, data["part2_solution"])

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

    def test_day5_part1(self):
        """Day 5 Part 1 Test Case."""
        data = self.testData["day-5"]
        # test find_closest_location
        closest_location = min(calculations.find_locations(data["test_input"]))
        self.assertEqual(closest_location, data["part1_solution"])
    
    def test_day5_part2(self):
        """Day 5 Part 2 Test Case."""
        data = self.testData["day-5"]
        # test find_closest_location
        location_ranges = calculations.find_location_ranges(data["test_input"])
        closest_location = min(location["start"] for location in location_ranges)
        self.assertEqual(closest_location, data["part2_solution"])
    
    def test_day6_part1(self):
        """Day 6 Part 1 Test Case."""
        data = self.testData["day-6"]
        beat_records = calculations.find_beat_records(data["test_input"])
        self.assertEqual(prod(beat_records), data["part1_solution"])
    
    def test_day6_part2(self):
        """Day 6 Part 2 Test Case."""
        data = self.testData["day-6"]
        self.assertEqual(calculations.handle_big_race(data["test_input"]), data["part2_solution"])

    def test_day7_part1(self):
        """Day 7 Part 1 Test Case."""
        data = self.testData["day-7"]
        self.assertEqual(calculations.get_total_winnings(data["test_input"], 1), data["part1_solution"])

    def test_day7_part2(self):
        """Day 7 Part 2 Test Case."""
        data = self.testData["day-7"]
        self.assertEqual(calculations.get_total_winnings(data["test_input"], 2), data["part2_solution"])

    def test_day8_part1(self):
        """Day 8 Part 1 Test Cases."""
        cases = [
            {"case": "No repeat", "input_path": "./inputs/test/day8-1.txt", "output": 2},
            {"case": "Need to repeat", "input_path": "./inputs/test/day8-2.txt", "output": 6}
        ]
        for case in cases:
            with self.subTest(case["case"]):
                self.assertEqual(calculations.find_steps(case["input_path"]), case["output"])

    def test_day8_part2(self):
        """Day 8 Part 2 Test Case."""
        data = self.testData["day-8"]
        self.assertEqual(lcm(*calculations.find_ghost_steps(data["test_input"])), data["part2_solution"])
    
    def test_day9_part1(self):
        """Day 9 Part 1 Test Case."""
        data = self.testData["day-9"]
        self.assertEqual(sum(calculations.find_end_extrapolations(data["test_input"])), data["part1_solution"])

    def test_day9_part2(self):
        """Day 9 Part 1 Test Case."""
        data = self.testData["day-9"]
        self.assertEqual(sum(calculations.find_start_extrapolations(data["test_input"])), data["part2_solution"])

    def test_day10_part1(self):
        """Day 10 Part 1 Test Cases."""
        data = self.testData["day-10"]
        cases = [
            {"case": "Simple loop", "index": 0},
            {"case": "Complex loop", "index": 1}
        ]
        for case in cases:
            with self.subTest(case["case"]):
                self.assertEqual(calculations.find_farthest_pipe(data["test_inputs"][case["index"]]), data["part1_solutions"][case["index"]])

    def test_day11_part1(self):
        """Day 11 Part 1 Test Case."""
        data = self.testData["day-11"]
        self.assertEqual(sum(calculations.traverse_galaxies(data["test_input"], 1)), data["part1_solution"])

    def test_day11_part2(self):
        """Day 11 Part 2 Test Case."""
        data = self.testData["day-11"]
        cases = [
            {"case": "Small expansion (Part 1)", "index": 0},
            {"case": "Medium expansion", "index": 1},
            {"case": "Large expansion", "index": 2}
        ]
        for case in cases:
            with self.subTest(case["case"]):
                self.assertEqual(sum(calculations.traverse_galaxies(data["test_input"], 2, data["part2_constants"][case["index"]])), 
                                 data["part2_solutions"][case["index"]])

    def test_day12_part1(self):
        """Day 12 Part 1 Test Case."""
        data = self.testData["day-12"]
        self.assertEqual(sum(calculations.find_possible_arrangements(data["test_input"])), data["part1_solution"])

    def test_day13_part1(self):
        """Day 13 Part 1 Test Case."""
        data = self.testData["day-13"]
        self.assertEqual(calculations.find_mirror_summary(data["test_input"], 1), data["part1_solution"])
    
    def test_day13_part2(self):
        """Day 13 Part 2 Test Case."""
        data = self.testData["day-13"]
        self.assertEqual(calculations.find_mirror_summary(data["test_input"], 2), data["part2_solution"])

    # def test_day14_part1(self):
    #     """Day 14 Part 1 Test Case."""
    #     data = self.testData["day-14"]
    #     self.assertEqual(calculations.find_rock_load(data["test_input"]), data["part1_solution"])
        
    def test_day15_hash_algorithm(self):
        """Day 15 Part 1 HASH algorithm function test."""
        self.assertEqual(calculations.run_hash_algorithm("HASH"), 52)

    def test_day15_part1(self):
        """Day 15 Part 1 Test Case."""
        data = self.testData["day-15"]
        self.assertEqual(calculations.find_hash_sum(data["test_input"]), data["part1_solution"])
    
    def test_day15_part2(self):
        """Day 15 Part 2 Test Case."""
        data = self.testData["day-15"]
        self.assertEqual(calculations.find_focusing_power(data["test_input"]), data["part2_solution"])

    def test_day16_part1(self):
        """Day 16 Part 1 Test Case."""
        data = self.testData["day-16"]
        self.assertEqual(calculations.find_energized_tiles(data["test_input"]), data["part1_solution"])

    def test_day16_part2(self):
        """Day 16 Part 2 Test Case."""
        data = self.testData["day-16"]
        self.assertEqual(calculations.find_energized_tiles(data["test_input"], 2), data["part2_solution"])

if __name__ == '__main__':
    unittest.main()


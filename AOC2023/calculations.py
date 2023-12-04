from config import DIGIT_STRINGS

import re

#
## DAY 1 FUNCTIONS
#

def find_calibrations(file_data: list[str]) -> list[int]:
    """Parses a TXT document to return a list of calibration values based on digits."""
    calibration_values = []
    for line in file_data:
        digits = [char for char in line if char.isdigit()]
        calibration_value = int(digits[0])*10 + int(digits[-1])
        calibration_values.append(calibration_value)     

    return calibration_values           

def get_first_digit(line: str) -> int:
    """Checks a string for the first instance of either a digit 
    or digit-representative string.
    """
    string_to_check = ""
    for char in line:
        if char.isdigit():
            return(int(char))
        string_to_check += char
        for str in DIGIT_STRINGS:
            if str in string_to_check:
                return int(DIGIT_STRINGS[str])
                
def get_last_digit(line: str) -> int:
    """Checks a string from back to front the first instance of either a digit 
    or digit-representative string.
    """
    string_to_check = ""
    for char in reversed(line):
        if char.isdigit():
            return(int(char))
        string_to_check = char + string_to_check
        for str in DIGIT_STRINGS:
            if str in string_to_check:
                return int(DIGIT_STRINGS[str])

                    
def find_calibrations_with_strings(file_data: list[str]) -> list[int]:
    calibration_values = []
    for line in file_data:
        calibration_value = get_first_digit(line)*10 + get_last_digit(line)
        calibration_values.append(calibration_value)     
    
    return calibration_values

# SOLUTIONS

with open('inputs/day1.txt', newline='') as file:
    file_data = file.readlines()

day1_part1 = sum(find_calibrations(file_data))
day1_part2 = sum(find_calibrations_with_strings(file_data))
print(f"Day 1 - Part 1: {day1_part1}")
print(f"Day 1 - Part 2: {day1_part2}")

#
## DAY 2 FUNCTIONS
#

# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
# pattern is [str int: int str, int str; int str, int str, int str]

def find_max_colors(game_data) -> dict[str, int]:
    """Parses a TXT document of game data to return a dictionary of colors and their maximum number."""
    max_colors = {"red": [], "blue": [], "green": []}
    # separate rounds
    rounds = game_data.split(":")[1].split(";")
    for round in rounds:
        pairs = round.split(",")
        for pair in pairs:
            #separate colors
            color = pair.split(" ")[-1].strip()
            max_colors[color].append(int(pair.split(" ")[1]))
        # determine whether the game was possible
    return {
        "red": max(max_colors["red"]), 
        "blue": max(max_colors["blue"]), 
        "green": max(max_colors["green"])
    }


def find_possible_games(file_data: list[str], red_limit: int, green_limit: int, blue_limit: int) -> list[int]:
    """Parses a TXT document to return a list of possible games given a number of red, green, and blue cubes."""
    possible_games = []
    for game in file_data:
        # separate game number
        game_num = int(game.split(":")[0].split(" ")[1])
        # separate rounds
        max_colors = find_max_colors(game)
        # determine whether the game was possible
        if max_colors["red"] <= red_limit and max_colors["blue"] <= blue_limit and max_colors["green"] <= green_limit:
            possible_games.append(game_num)

    return possible_games

def find_minimum_cubes_power(file_data: list[str]) -> list[int]:
    """Parse a TXT document to determine minimum number of cubes to make a game possible."""
    minimum_cubes_power = []
    for game in file_data:
        # separate rounds
        max_colors = find_max_colors(game)
        # determine whether the game was possible
        minimum_cubes_power.append(max_colors["red"] * max_colors["blue"] * max_colors["green"])
    
    return minimum_cubes_power

# SOLUTIONS

with open('inputs/day2.txt', newline='') as file:
    file_data = file.readlines()

day2_part1 = sum(find_possible_games(file_data, 12, 13, 14))
day2_part2 = sum(find_minimum_cubes_power(file_data))
print(f"Day 2 - Part 1: {day2_part1}")
print(f"Day 2 - Part 2: {day2_part2}")

#
# DAY 3 FUNCTIONS
#

def check_adjacency(truthy_grid: list[list[bool]], coords: list[dict]) -> list[bool]:
    """Check coordinates against a grid of truthiness to determine whether a group of characters
    is adjacent to a truthy value.
    """
    adjacency = []
    for coord in coords:
        # remember truthy grid has padding
        row = coord["row"] + 1
        start = coord["start"] + 1
        end = coord["end"] + 1
        # check horizontal adjacency - remember truthy grid has padding row/column
        horizontal = truthy_grid[row][start - 1] or truthy_grid[row][end + 1]
        # check vertical adjacency
        # NOTE: I don't actually know why I need to add by 2 here, this worked on accident??
        vertical = any(truthy_grid[row - 1][start - 1:end + 2]) or any(truthy_grid[row + 1][start - 1:end + 2])
        adjacency.append(bool(horizontal or vertical))

    return adjacency

def find_part_numbers(grid: list[str]) -> list[int]:
    """Parse a grid to determine "part numbers"
    i.e., Numbers that are non-adjacent (up/down/left/right/diagonal) to a symbol.
    """
    number_info, part_numbers = [], []
    # the truthy grid should have a padding row/column to surround edges
    truthy_grid = [[False for char in grid[0]]]
    for row in grid:
        new_row = [False]
        for char in row:
            if char == '.' or char.isdigit():
                new_row.append(False)
            else:
                new_row.append(True)
        new_row.append(False)
        truthy_grid.append(new_row)
    truthy_grid.append([False for char in grid[0]])
    # find the numbers
    for i, row in enumerate(grid):
        numbers = re.finditer('\d+',row)
        for number in numbers:
            # get coordinates
            number_info.append({
                "number": int(number.group()),
                "row": i, 
                "start": number.start(), 
                "end": number.end() - 1
                })
    adjacency = check_adjacency(truthy_grid, number_info)
    for i, number in enumerate(number_info):
        if adjacency[i]:
            part_numbers.append(number["number"])

    return part_numbers

def find_adjacent_parts(asterisk_info: list[dict], number_info: list[dict]) -> list[list[int]]:
    """Match asterisks to part numbers adjacent to them."""
    adjacent_parts = [[] for asterisk in asterisk_info]
    for i, asterisk in enumerate(asterisk_info):
        for number in number_info:
            # check for horizontal adjacency
            if asterisk["row"] - 1 <= number["row"] <= asterisk["row"] + 1:
                if number["start"] - 1 <= asterisk["col"] <= number["end"] + 1:
                    adjacent_parts[i].append(number["number"])

    return adjacent_parts

def find_gear_ratios(grid: list[str]) -> list[int]:
    """Parse a grid to determine gears
    i.e., asterisks that are adjacent to exactly two part numbers.
    """
    asterisk_info, number_info, gear_ratios = [], [], []
    # find all of the asterisks and numbers
    for i, row in enumerate(grid):
        asterisks = re.finditer('\\*', row)
        numbers = re.finditer('\d+', row)
        for asterisk in asterisks:
            # get coordinates
            asterisk_info.append({
                "row": i,
                "col": asterisk.start()
            })
        for number in numbers:
            # get coordinates
            number_info.append({
                "number": int(number.group()),
                "row": i, 
                "start": number.start(), 
                "end": number.end() - 1
                })
    adjacent_parts = find_adjacent_parts(asterisk_info, number_info)
    for i, parts in enumerate(adjacent_parts):
        if len(adjacent_parts[i]) == 2:
            gear_ratios.append(parts[0] * parts[1])
        
    return gear_ratios

with open('inputs/day3.txt', newline='') as file:
    file_data = file.read()
    line_data = file_data.split('\n')

day3_part1 = sum(find_part_numbers(line_data))
day3_part2 = sum(find_gear_ratios(line_data))
print(f"Day 3 - Part 1: {day3_part1}")
print(f"Day 3 - Part 2: {day3_part2}")

#
# DAY 4 FUNCTIONS
#

def find_winners(card_info: str) -> int:
    """Parse a string of card info to determine number of winning numbers."""
    winning_numbers = [int(num) for num in card_info.split(":")[1].split("|")[0].split(" ") if num != '']
    my_numbers = [int(num) for num in card_info.split(":")[1].split("|")[1].split(" ") if num != '']
    winners = 0
    for number in my_numbers:
        if number in winning_numbers:
            winners += 1
    
    return winners
    
def find_card_scores(card_data: list[str]) -> list[int]:
    """Parse a TXT file of card info to determine the scores of cards."""
    card_scores = []
    for card in card_data:
        card_scores.append(2**(find_winners(card) - 1) if find_winners(card) > 0 else 0)

    return card_scores

def find_total_copies(card_data: list[str]) -> list[int]:
    """Parse a TXT file of card info to determine the total copies of each card."""
    total_copies = [1 for card in card_data]
    for i, copies in enumerate(total_copies):
        winners = find_winners(card_data[i])
        for j in range(1, winners + 1):
            total_copies[i + j] += copies

    return total_copies

with open('inputs/day4.txt', newline='') as file:
    file_data = file.read()
    card_data = file_data.split('\n')

day4_part1 = sum(find_card_scores(card_data))
day4_part2 = sum(find_total_copies(card_data))
print(f"Day 4 - Part 1: {day4_part1}")
print(f"Day 4 - Part 2: {day4_part2}")


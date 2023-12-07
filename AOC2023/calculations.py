from config import DIGIT_STRINGS

from math import prod
import re
import time

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

start_time = time.time()
day1_part1 = sum(find_calibrations(file_data))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 1 - Part 1: {day1_part1}  {exec_time}ms")
start_time = time.time()
day1_part2 = sum(find_calibrations_with_strings(file_data))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 1 - Part 2: {day1_part2}  {exec_time}ms")

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

start_time = time.time()
day2_part1 = sum(find_possible_games(file_data, 12, 13, 14))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 2 - Part 1: {day2_part1}  {exec_time}ms")
start_time = time.time()
day2_part2 = sum(find_minimum_cubes_power(file_data))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 2 - Part 2: {day2_part2}  {exec_time}ms")

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
        vertical = any(truthy_grid[row - 1][start - 1:end + 2]) or any(truthy_grid[row + 1][start - 1:end + 2])
        adjacency.append(bool(horizontal or vertical))

    return adjacency

def find_part_numbers(grid: list[str]) -> list[int]:
    """Parse a grid to determine "part numbers"
    i.e., Numbers that are non-adjacent (up/down/left/right/diagonal) to a symbol.
    """
    number_info, part_numbers = [], []
    # the truthy grid should have a padding row/column to surround edges
    truthy_grid = [[False for char in grid[0]] + [False]] 
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

# SOLUTIONS

with open('inputs/day3.txt', newline='') as file:
    file_data = file.read()
    line_data = file_data.split('\n')

start_time = time.time()
day3_part1 = sum(find_part_numbers(line_data))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 3 - Part 1: {day3_part1}  {exec_time}ms")
start_time = time.time()
day3_part2 = sum(find_gear_ratios(line_data))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 3 - Part 2: {day3_part2}  {exec_time}ms")

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

# SOLUTIONS

with open('inputs/day4.txt', newline='') as file:
    file_data = file.read()
    card_data = file_data.split('\n')

start_time = time.time()
day4_part1 = sum(find_card_scores(card_data))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 4 - Part 1: {day4_part1}  {exec_time}ms")
start_time = time.time()
day4_part2 = sum(find_total_copies(card_data))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 4 - Part 2: {day4_part2}  {exec_time}ms")

#
# DAY 5 FUNCTIONS
#

def map_x_to_y(map_info: list[list[str]], initial_list: list[int]) -> list[int]:
    new_list = initial_list
    for i, x in enumerate(initial_list):
        for mapping in map_info:
            dest_start = int(mapping[0])
            source_start = int(mapping[1])
            range_length = int(mapping[2])
            diff = x - source_start
            if 0 <= diff <= range_length - 1:
                new_list[i] = dest_start + diff
                break
            else:
                continue
    return new_list

def find_locations(almanac_path: str):
    """Parses TXT file and returns locations for planting individual seeds."""
    with open(almanac_path, newline='') as file:
        file_data = file.read()
        almanac_sections = file_data.split('\n\n')

    almanac = {}
    seeds_row = almanac_sections[0]
    almanac["seeds"] = [int(seeds) for seeds in seeds_row.split(": ")[1].split(" ")]
    for section in almanac_sections[1:]:
        sub_sections = section.split("\n")
        almanac[sub_sections[0].replace(":", "")] = [list.split(" ") for list in sub_sections[1:]]
    
    soils = map_x_to_y(almanac["seed-to-soil map"], almanac["seeds"])
    fertilizers = map_x_to_y(almanac["soil-to-fertilizer map"], soils)
    waters = map_x_to_y(almanac["fertilizer-to-water map"], fertilizers)
    lights = map_x_to_y(almanac["water-to-light map"], waters)
    temps = map_x_to_y(almanac["light-to-temperature map"], lights)
    humidities = map_x_to_y(almanac["temperature-to-humidity map"], temps)
    locations = map_x_to_y(almanac["humidity-to-location map"], humidities) 

    return locations

def map_ranges(map_info: list[list[str]], input_range_info: list[dict]):
    """Maps a range (start, end) to another range (start, end) or ranges."""
    output_range = []
    # 1 2 3 4 5 6 7 8
    #   2 3 4   6 7 8 9 10
    # 1-2 2-4 4-6 6-7 7-8
    
    for input_range in input_range_info:
        for mapping in map_info:
            last_mapping = mapping == map_info[-1]
            range_length = int(mapping[2])
            source_start = int(mapping[1])
            source_end = source_start + range_length - 1
            dest_start = int(mapping[0])
            dest_end = dest_start + range_length - 1
            # there are 5 cases:
            # 1. initial range is completely within mapping range
            if source_start <= input_range["start"] and input_range["end"] <= source_end:
                output_range.append({
                    "start": dest_start + (input_range["start"] - source_start),
                    "end": dest_end + (input_range["end"] - source_end),
                })
                break
            # 2. initial range is completely outside of mapping range
            elif input_range["end"] <= source_start or source_end <= input_range["start"]:
                # check for final mapping
                if last_mapping:
                    output_range.append(input_range)
                # check more mappings if not final mapping
                continue
            # 3. mapping range is completely within initial range
            elif input_range["start"] <= source_start and source_end <= input_range["end"]:
                # handle section within mapping range
                output_range.append({
                    "start": dest_start,
                    "end": dest_end
                })
                # handle sections before and after match
                if last_mapping:
                    output_range.append({
                        "start": input_range["start"],
                        "end": source_start - 1
                        })
                    output_range.append({
                        "start": source_end + 1,
                        "end": input_range["end"]
                        })
                    continue
                input_range_info.append({
                    "start": input_range["start"],
                    "end": source_start - 1
                    })
                input_range_info.append({
                    "start": source_end + 1,
                    "end": input_range["end"]
                    })
                break
            # 4. mapping range overlaps with beginning of initial range
            elif source_start <= input_range["start"] <= source_end <= input_range["end"]:
                # handle section within mapping range
                output_range.append({
                    "start": dest_start + (input_range["start"] - source_start),
                    "end": dest_end
                })
                # handle section after match
                if last_mapping:
                    output_range.append({
                        "start": source_end + 1,
                        "end": input_range["end"]
                        })
                    continue
                input_range_info.append({
                    "start": source_end + 1,
                    "end": input_range["end"]
                    })
                break
            # 5. mapping range overlaps with end of initial range
            elif input_range["start"] <= source_start <= input_range["end"] <= source_end:
                # handle section within mapping range
                output_range.append({
                    "start": dest_start,
                    "end": dest_end + (input_range["end"] - source_end)
                })
                # handle section before match
                if last_mapping:
                    output_range.append({
                        "start": input_range["start"],
                        "end": source_start - 1
                        })
                    continue
                input_range_info.append({
                    "start": input_range["start"],
                    "end": source_start - 1
                    })
                break
            else:
                raise("This shouldn't be possible")
    
    return output_range

def find_location_ranges(almanac_path: str):
    """Parses a TXT file to find ranges of seed planting locations."""
    with open(almanac_path, newline='') as file:
        file_data = file.read()
        almanac_sections = file_data.split('\n\n')

    almanac = {}
    seeds_row = almanac_sections[0]
    almanac["seeds"] = []
    seed_map = [int(seeds) for seeds in seeds_row.split(": ")[1].split(" ")]
    for i in range(0, len(seed_map), 2):
        almanac["seeds"].append({
            "start": seed_map[i],
            "end": seed_map[i] + seed_map[i + 1] - 1,
        })
    for section in almanac_sections[1:]:
        sub_sections = section.split("\n")
        almanac[sub_sections[0].replace(":", "")] = [list.split(" ") for list in sub_sections[1:]]
    
    soil_ranges = map_ranges(almanac["seed-to-soil map"], almanac["seeds"])
    fertilizer_ranges = map_ranges(almanac["soil-to-fertilizer map"], soil_ranges)
    water_ranges = map_ranges(almanac["fertilizer-to-water map"], fertilizer_ranges)
    light_ranges = map_ranges(almanac["water-to-light map"], water_ranges)
    temp_ranges = map_ranges(almanac["light-to-temperature map"], light_ranges)
    humidity_ranges = map_ranges(almanac["temperature-to-humidity map"], temp_ranges)
    location_ranges = map_ranges(almanac["humidity-to-location map"], humidity_ranges) 

    return location_ranges

# SOLUTIONS

start_time = time.time()
day5_part1 = min(find_locations('inputs/day5.txt'))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 5 - Part 1: {day5_part1}  {exec_time}ms")
location_ranges = find_location_ranges('inputs/day5.txt')
start_time = time.time()
day5_part2 = min(location["start"] for location in location_ranges)
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 5 - Part 2: {day5_part2}  {exec_time}ms")

#
# DAY 6
#

def find_beat_records(race_data: str) -> list[int]:
    """Given race times and record distances as a string, 
    return list of number of ways you could beat the record for each race.
    """
    # M entries (3)
    races, beat_records = [], []
    times = race_data.splitlines()[0].split(":")[1].split()
    records = race_data.splitlines()[1].split(":")[1].split()
    
    for t, distance in zip(times, records):
        races.append({
            "time": int(t),
            "record": int(distance)
        })
    # O(M*N)
    for race in races:
        beats = find_ways_to_beat(race) #O(N)
        beat_records.append(beats)

    return beat_records

def find_ways_to_beat(race_info: dict) -> int:
    """Given race data (time and distance to beat), return the number of ways you could beat the record."""
    beats = 0
    # Time complexity on this one?
    # O(N) N is the max Time
    # Pseudo-linear - Actually Exponential
    # How do we speed it up?
    # get the quadratic equation -> minh maxh
    # maxh - minh = ways to beat. AND SOME EASY EXTRA WORK
    # O(K) = O(1) constant time
    for t in range(race_info["time"] + 1):
        hold_t = t
        travel_t = race_info["time"] - t
        speed = hold_t
        distance = speed * travel_t
        if distance > race_info["record"]:
            beats += 1
    
    return beats

def handle_big_race(race_data: str) -> int:
    # M entries on times / distances -> M=1
    # 
    time = race_data.splitlines()[0].split(":")[1].replace(" ","")
    record = race_data.splitlines()[1].split(":")[1].replace(" ","")
    race = {"time": int(time), "record": int(record)}
    # O(N) -
    # 4 digits, what's the maximum value T that you cna have?
    # 9999= 10K
    # 5 digits,
    # 99999 = 100K
    # M digits
    # 10^M
    beats = find_ways_to_beat(race)

    return beats

# SOLUTIONS

with open('./inputs/day6.txt', newline='') as file:
    race_data = file.read()

start_time = time.time()
day6_part1 = prod(find_beat_records(race_data))
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 6 - Part 1: {day6_part1}  {exec_time}ms")
start_time = time.time()
day6_part2 = handle_big_race(race_data)
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 6 - Part 2: {day6_part2}  {exec_time}ms")

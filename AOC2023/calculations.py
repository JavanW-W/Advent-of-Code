import config
from math import prod, lcm, comb, floor, ceil
from itertools import product, combinations
from statistics import mode
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
        for str in config.DIGIT_STRINGS:
            if str in string_to_check:
                return int(config.DIGIT_STRINGS[str])
                
def get_last_digit(line: str) -> int:
    """Checks a string from back to front the first instance of either a digit 
    or digit-representative string.
    """
    string_to_check = ""
    for char in reversed(line):
        if char.isdigit():
            return(int(char))
        string_to_check = char + string_to_check
        for str in config.DIGIT_STRINGS:
            if str in string_to_check:
                return int(config.DIGIT_STRINGS[str])

                    
def find_calibrations_with_strings(file_data: list[str]) -> list[int]:
    calibration_values = []
    for line in file_data:
        calibration_value = get_first_digit(line)*10 + get_last_digit(line)
        calibration_values.append(calibration_value)     
    
    return calibration_values

# SOLUTIONS

# with open('inputs/day1.txt', newline='') as file:
#     file_data = file.readlines()

# start_time = time.time()
# day1_part1 = sum(find_calibrations(file_data))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 1 - Part 1: {day1_part1}  {exec_time}ms")
# start_time = time.time()
# day1_part2 = sum(find_calibrations_with_strings(file_data))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 1 - Part 2: {day1_part2}  {exec_time}ms")

#
## DAY 2 FUNCTIONS
#

# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
# pattern is [str int: int str, int str; int str, int str, int str]

def find_max_colors(game_data) -> dict[str, int]:
    """Parses a TXT document of game data to return a dictionary of colors and their maximum number."""
    max_colors: dict = {"red": [], "blue": [], "green": []}
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

# with open('inputs/day2.txt', newline='') as file:
#     file_data = file.readlines()

# start_time = time.time()
# day2_part1 = sum(find_possible_games(file_data, 12, 13, 14))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 2 - Part 1: {day2_part1}  {exec_time}ms")
# start_time = time.time()
# day2_part2 = sum(find_minimum_cubes_power(file_data))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 2 - Part 2: {day2_part2}  {exec_time}ms")

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
    adjacent_parts: list[list] = [[] for asterisk in asterisk_info]
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

# with open('inputs/day3.txt', newline='') as file:
#     file_data = file.read()
#     line_data = file_data.split('\n')

# start_time = time.time()
# day3_part1 = sum(find_part_numbers(line_data))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 3 - Part 1: {day3_part1}  {exec_time}ms")
# start_time = time.time()
# day3_part2 = sum(find_gear_ratios(line_data))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 3 - Part 2: {day3_part2}  {exec_time}ms")

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

# with open('inputs/day4.txt', newline='') as file:
#     file_data = file.read()
#     card_data = file_data.split('\n')

# start_time = time.time()
# day4_part1 = sum(find_card_scores(card_data))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 4 - Part 1: {day4_part1}  {exec_time}ms")
# start_time = time.time()
# day4_part2 = sum(find_total_copies(card_data))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 4 - Part 2: {day4_part2}  {exec_time}ms")

#
# DAY 5 FUNCTIONS
#

def map_x_to_y(map_info: list, initial_list: list[int]) -> list[int]:
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

    almanac: dict = {}
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

# start_time = time.time()
# day5_part1 = min(find_locations('inputs/day5.txt'))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 5 - Part 1: {day5_part1}  {exec_time}ms")
# location_ranges = find_location_ranges('inputs/day5.txt')
# start_time = time.time()
# day5_part2 = min(location["start"] for location in location_ranges)
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 5 - Part 2: {day5_part2}  {exec_time}ms")

#
# DAY 6
#

def find_beat_records(race_data: str) -> list[int]:
    """Given race times and record distances as a string, 
    return list of number of ways you could beat the record for each race.
    """
    races, beat_records = [], []
    times = race_data.splitlines()[0].split(":")[1].split()
    records = race_data.splitlines()[1].split(":")[1].split()
    for t, distance in zip(times, records):
        races.append({
            "time": int(t),
            "record": int(distance)
        })

    for race in races:
        beats = find_ways_to_beat(race)
        beat_records.append(beats)

    return beat_records

def find_ways_to_beat(race_info: dict) -> int:
    """Given race data (time and distance to beat), return the number of ways you could beat the record."""
    beats = 0
    for t in range(race_info["time"] + 1):
        hold_t = t
        travel_t = race_info["time"] - t
        speed = hold_t
        distance = speed * travel_t
        if distance > race_info["record"]:
            beats += 1
    
    return beats

def handle_big_race(race_data: str) -> int:
    time = race_data.splitlines()[0].split(":")[1].replace(" ","")
    record = race_data.splitlines()[1].split(":")[1].replace(" ","")
    race = {"time": int(time), "record": int(record)}
    beats = find_ways_to_beat(race)

    return beats

# SOLUTIONS

# with open('./inputs/day6.txt', newline='') as file:
#     race_data = file.read()

# start_time = time.time()
# day6_part1 = prod(find_beat_records(race_data))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 6 - Part 1: {day6_part1}  {exec_time}ms")
# start_time = time.time()
# day6_part2 = handle_big_race(race_data)
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 6 - Part 2: {day6_part2}  {exec_time}ms")

#
# DAY 7 FUNCTIONS
#

def get_ranks(hand_data: list[str], part: int) -> list[int]:
    """Given a list of hand data, find corresponding strength rankings.
    
    Hand types in order of strongest to weakest:
    5 of a kind
    4 of a kind
    Full House (2 of a kind + 3 of a kind)
    3 of a kind
    2 pair
    1 pair
    High card
    """
    ranks, ids = [], []
    for hand in hand_data:
        hand_val = [config.CARD_VALUES[card] for card in hand]
        if part == 2 and 'J' in hand:
            for i, val in enumerate(hand_val):
                hand_val[i] = 14 if val == 4 else val
            try:
                hand = hand.replace('J', mode(hand.replace('J','')))
            except Exception: # the case that your hand is 'JJJJJ'
                pass
        counts = [hand.count(card) for card in set(hand)]
        assert(sum(counts) == 5)
        if counts.count(5) == 1:
            ids.append([1] + [hand_val])
        elif counts.count(4) == 1:
            ids.append([2] + [hand_val])
        elif counts.count(3) == 1:
            if counts.count(2) == 1:
                ids.append([3] + [hand_val])
            else:
                ids.append([4] + [hand_val])
        elif counts.count(2) == 2:
            ids.append([5] + [hand_val])
        elif counts.count(2) == 1:
            ids.append([6] + [hand_val])
        elif counts.count(1) == 5:
            ids.append([7] + [hand_val])
    
    for num in ids:
        ranks.append(sorted(ids, reverse=True).index(num) + 1)

    return ranks 

def get_total_winnings(hand_data: list[str], part: int) -> int:
    """Given a list of hands and bids, calculate total winnings."""
    winnings = []
    hands = [hand.strip()[:5] for hand in hand_data]
    bids = [int(hand.strip()[5:]) for hand in hand_data]
    ranks = get_ranks(hands, part)
    for bid, rank in zip(bids, ranks):
        winnings.append(bid * rank)
    
    return sum(winnings)

# SOLUTIONS

with open('./inputs/day7.txt', newline='') as file:
    hand_data = file.readlines()

# start_time = time.time()
# day7_part1 = get_total_winnings(hand_data, 1)
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 7 - Part 1: {day7_part1}  {exec_time}ms")
# start_time = time.time()
# day7_part2 = get_total_winnings(hand_data, 2)
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 7 - Part 2: {day7_part2}  {exec_time}ms")

#
# DAY 8 FUNCTIONS
#

def find_steps(input_path: str) -> int:
    """Given a map of nodes and left/right instructions, find how many steps it takes to get to ZZZ."""
    with open(input_path, newline='') as file:
        map_data = file.readlines()

    instructions = map_data[0].replace('L','0').replace('R','1').strip()
    network = {}
    for line in map_data[2:]:
        network[line.split("=")[0].strip()] = line.split("=")[1].strip().replace(' ','').replace('(','').replace(')','').split(",")

    current_node = 'AAA'
    step = 0
    while current_node != 'ZZZ':
        go = step % len(instructions)
        next_node = network[current_node][int(instructions[go])]
        step += 1
        current_node = next_node

    return step

def find_ghost_steps(input_path: str) -> list[int]:
    """Given a map of nodes and left/right instructions, find how many steps it takes for a ghost to get from all 
    positions that end with A to all positions that end with Z.
    """
    with open(input_path, newline='') as file:
        map_data = file.readlines()

    instructions = map_data[0].replace('L','0').replace('R','1').strip()
    network = {}
    for line in map_data[2:]:
        network[line.split("=")[0].strip()] = line.split("=")[1].strip().replace(' ','').replace('(','').replace(')','').split(",")

    a_regex = re.compile("..A")
    a_nodes = set(filter(a_regex.match, network.keys()))
    steps = []
    for node in a_nodes:
        step = 0
        current_node = node
        while current_node[-1] != 'Z':
            go = step % len(instructions)
            next_node = network[current_node][int(instructions[go])]
            step += 1
            current_node = next_node
        steps.append(step)

    return steps


# SOLUTIONS

# start_time = time.time()
# day8_part1 = find_steps('./inputs/day8.txt')
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 8 - Part 1: {day8_part1}  {exec_time}ms")
# start_time = time.time()
# day8_part2 = lcm(*find_ghost_steps('./inputs/day8.txt'))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 8 - Part 2: {day8_part2}  {exec_time}ms")

#
# DAY 9 FUNCTIONS
#

def find_start_extrapolations(input_path: str) -> list[int]:
    with open(input_path, newline='') as file:
        oasis_data = file.readlines()

    before_values = []
    for line in oasis_data:
        values = line.split(" ")
        first_vals = []
        while True:
            deltas = []
            first_vals.append(int(values[0]))
            for i in range(1, len(values)):
                deltas.append(int(values[i]) - int(values[i-1]))
            if set(deltas) == {0}:
                break
            values = deltas
        extrap_vals = [0]
        for i in range(len(first_vals)):
            extrap_vals.append(first_vals[-1 - i] - extrap_vals[i])

        before_values.append(extrap_vals[-1])      

    return before_values

def find_end_extrapolations(input_path: str) -> list[int]:
    with open(input_path, newline='') as file:
        oasis_data = file.readlines()

    next_values = []
    for line in oasis_data:
        values = line.split(" ")
        last_vals = []
        while True:
            deltas = []
            last_vals.append(int(values[-1]))
            for i in range(1, len(values)):
                deltas.append(int(values[i]) - int(values[i-1]))
            if set(deltas) == {0}:
                break
            values = deltas  

        next_values.append(sum(last_vals))      

    return next_values

# SOLUTIONS

# start_time = time.time()
# day9_part1 = sum(find_end_extrapolations('./inputs/day9.txt'))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 9 - Part 1: {day9_part1}  {exec_time}ms")
# start_time = time.time()
# day9_part2 = sum(find_start_extrapolations('./inputs/day9.txt'))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 9 - Part 2: {day9_part2}  {exec_time}ms")

#
# DAY 10 FUNCTIONS
#

def find_farthest_pipe(input_path: str) -> int:
    """Given a map of pipes with a creature in it, find how many steps away the farthest section of pipe is from the creature."""
    with open(input_path, newline='') as file:
        map_data = file.readlines()

    # find starting point
    for row, line in enumerate(map_data):
        try:
            starting_point = {"row": row, "col": line.index("S")}
        except ValueError:
            continue

    
    # check all directions to initialize loop
    direction_points = []
    up = map_data[starting_point["row"] - 1][starting_point["col"]]
    right = map_data[starting_point["row"]][starting_point["col"] + 1]
    down = map_data[starting_point["row"] + 1][starting_point["col"]]
    left = map_data[starting_point["row"]][starting_point["col"] - 1]
    if "up" in config.PIPES[up]:
        direction_points.append({
            "move": "up",
            "row": starting_point["row"] - 1,
            "col": starting_point["col"]
        })
    if "right" in config.PIPES[right]:
        direction_points.append({
            "move": "right",
            "row": starting_point["row"],
            "col": starting_point["col"] + 1
        })
    if "down" in config.PIPES[down]:
        direction_points.append({
            "move": "down",
            "row": starting_point["row"] + 1,
            "col": starting_point["col"]
        })
    if "left" in config.PIPES[left]:
        direction_points.append({
            "move": "left",
            "row": starting_point["row"],
            "col": starting_point["col"] - 1
        })

    step = 0

    pipe_points = [starting_point, starting_point]
    while True:
        for index, (point, direction) in enumerate(zip(pipe_points, direction_points)):
            # what direction are you going in?
            going = direction["move"]
            # what is the character?
            pipe_type = map_data[direction["row"]][direction["col"]]
            # what are you doing?
            directions = config.PIPES[pipe_type][going]
            # your next pipe point will be your previous direction point
            next_point = {
                "row": direction["row"],
                "col": direction["col"],
            }
            next_direction = {
                "row": point["row"] + directions[0],
                "col": point["col"] + directions[1],
                "move": directions[2],
            }
            # reassign your pipe points
            pipe_points[index] = next_point
            direction_points[index] = next_direction

        step += 1

        if pipe_points[0] == pipe_points[1]:
            break

    return step

# SOLUTIONS

# start_time = time.time()
# day10_part1 = find_farthest_pipe('./inputs/day10.txt')
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 10 - Part 1: {day10_part1}  {exec_time}ms")

#
# DAY 11 FUNCTIONS
#

def expand_universe(galaxy_data: list[str]) -> list[str]:
    """Widen each row/column with no galaxy in it by 100%."""
    expanded_universe = []
    for row in galaxy_data:
        if "#" in row:
            expanded_universe.append(row)
        else:
            expanded_universe.extend([row]*2)
    expanded_universe = list(zip(*expanded_universe))  # transpose
    iter = enumerate(expanded_universe)
    for i, col in iter:
        if "#" not in col:
            expanded_universe.insert(i, col)
            next(iter)
    expanded_universe = list(zip(*expanded_universe))  # transpose
    expanded_universe = [''.join(i for i in row) for row in expanded_universe]
    return expanded_universe


def traverse_galaxies(input_path: str, part: int, expansion_constant: int = None) -> list[int]:
    """Given an observatory view, return list of shortest path between each pair of galaxies."""
    with open(input_path, newline='') as file:
        galaxy_data = file.readlines()

    if part == 1:
        galaxy_data = expand_universe(galaxy_data)
    elif part == 2:
        galaxy_data = [row.strip() for row in galaxy_data]

    # find coordinates of galaxies
    galaxies = []
    for i, row in enumerate(galaxy_data):
        for j, val in enumerate(row):
            if val == "#":
                galaxies.append((i,j))
    pairs = list(combinations(galaxies, 2))
    distances = []
    for pair in pairs:
        rows = sorted([pair[0][0], pair[1][0]])
        cols = sorted([pair[0][1], pair[1][1]])
        if part == 1:
            distances.append((rows[1] - rows[0]) + (cols[1] - cols[0]))
        if part == 2:
            # figure out how many empty rows/cols are between the pair
            row_expansions, col_expansions = 0, 0
            for i in range(rows[0], rows[1]):
                if "#" not in galaxy_data[i]:
                    row_expansions += 1
            trans_universe = list(zip(*galaxy_data))
            for i in range(cols[0], cols[1]) :
                if "#" not in trans_universe[i]:    
                    col_expansions += 1
            distances.append(rows[1] - rows[0] + row_expansions*(expansion_constant - 1)
                             + (cols[1] - cols[0] + col_expansions*(expansion_constant - 1)))
    
    return distances

# SOLUTIONS

# start_time = time.time()
# day11_part1 = sum(traverse_galaxies('./inputs/day11.txt', 1))
# exec_time = round(1000 * (time.time() - start_time), 4)
# # print(f"Day 11 - Part 1: {day11_part1}  {exec_time}ms")
# start_time = time.time()
# day11_part2 = sum(traverse_galaxies('./inputs/day11.txt', 2, 1000000))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 11 - Part 2: {day11_part2}  {exec_time}ms")

#
# DAY 12 FUNCTIONS
#

def find_possible_arrangements(input_path: str) -> list[int]:
    """Given a list of hot springs with unknown arrangements, return list of possible arrangements for each spring."""
    with open(input_path, newline='') as file:
        spring_data = file.readlines()

    num_arr = []
    for row in spring_data:
        # get info from the row
        conditions = [i for i in row.split(" ")[0]]
        contig_groups = [int(i.strip()) for i in row.split(" ")[1].split(",")]
        # make a regex for this for later
        regex_pattern ="\.*"
        for i, val in enumerate(contig_groups):
            if i == len(contig_groups) - 1:
                regex_pattern += f"{'#' * val}\.*"
            else:
                regex_pattern += f"{'#' * val}\.+"
        matches = 0
        # find all possible permutations of the unknown values
        unknowns = int(conditions.count("?"))
        perm = product('.#', repeat=unknowns)
        possibilities = [''.join(i) for i in list(perm)]
        # slot them into the ? indices and compare against the contig_groups regex
        indices = [i for i, x in enumerate(conditions) if x == "?"]
        for possibility in possibilities:
            for i, index in enumerate(indices):
                conditions[index] = possibility[i]
            match = re.fullmatch(regex_pattern, ''.join(conditions))
            if match:
                matches += 1
        num_arr.append(matches)

    return num_arr

# SOLUTIONS

# start_time = time.time()
# day12_part1 = sum(find_possible_arrangements('./inputs/day12.txt'))
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 12 - Part 1: {day12_part1}  {exec_time}ms")

#
# DAY 13 FUNCTIONS
#

def all_but_one(iterable) -> bool:
    """Returns true if all but one statement in the iterable is true."""
    truths = [result for result in iterable]
    if truths.count(False) == 1:
        return truths.index(False)
    else:
        return False

def find_mirror_summary(input_path: str, part: int) -> int:
    """Given a list of patterns, return the summary of notes re: mirror locations
    i.e., sum(number of columns to the left of each vertical line of reflection)
    + 100*(sum(number of rows above each horizontal line of reflection)).
    """
    with open(input_path, newline='') as file:
        pattern_data = file.read()

    # massage data
    # split up by each pattern
    horizontal_reflections, vertical_reflections = [], []
    patterns = [pattern.split('\n') for pattern in pattern_data.split('\n\n')]
    for x, pattern in enumerate(patterns):
        reflection_axis = 0
        search_over = False

        # check rows
        for i in range(len(pattern) - 1):
            # check for the edge case where the smudge is on the edge
            if part == 2:
                if all_but_one(pattern[i][j] == pattern[i+1][j] for j in range(len(pattern[i]))) is not False:
                    if i == 0:
                        horizontal_reflections.append(1)
                        search_over = True
                    elif i == len(pattern) - 2:
                        horizontal_reflections.append(len(pattern) - 1)
                        search_over = True
                    else:
                        reflection_axis = i + 0.5
                        # see if you're over the halfway point
                        if ceil(reflection_axis) > (len(pattern) - 1) / 2:
                            mirror_i = ceil(reflection_axis)
                            search_over = all_but_one(pattern[mirror_i - 1 - j] == pattern[mirror_i + j] for j in range(len(pattern) - mirror_i))
                            if search_over is not False:
                                horizontal_reflections.append(mirror_i)
                            else:
                                continue
                        else:
                            mirror_i = floor(reflection_axis)
                            search_over = all_but_one(pattern[mirror_i - j] == pattern[mirror_i + 1 + j] for j in range(mirror_i + 1))
                            if search_over is not False:
                                horizontal_reflections.append(mirror_i + 1)
                            else:
                                continue
                if search_over is not False:
                    break
            # check if it's the same as the one after
            if pattern[i] == pattern[i + 1]:
                # check for edge case where there is only one row above
                if i == 0 and part == 1:
                    horizontal_reflections.append(1)
                    search_over = True
                else:
                    reflection_axis = i + 0.5
                    # see if you're over the halfway point
                    if ceil(reflection_axis) > (len(pattern) - 1) / 2:
                        mirror_i = ceil(reflection_axis)
                        if part == 1:
                            search_over = all(pattern[mirror_i - 1 - j] == pattern[mirror_i + j] for j in range(len(pattern) - mirror_i))
                            if search_over is not False:
                                horizontal_reflections.append(mirror_i)
                            else:
                                continue
                        elif part == 2:
                            off_row = all_but_one(pattern[mirror_i - 1 - j] == pattern[mirror_i + j] for j in range(len(pattern) - mirror_i))
                            if off_row is not False:
                                index = list(range(len(pattern) - mirror_i))[off_row]
                                search_over = all_but_one(pattern[mirror_i - 1 - index][k] == pattern[mirror_i + index][k] for k in range(len(pattern[mirror_i + index])))
                                if search_over is not False:
                                    horizontal_reflections.append(mirror_i)
                                else:
                                    continue
                            else:
                                continue
                    else:
                        mirror_i = floor(reflection_axis)
                        if part == 1:
                            search_over = all(pattern[mirror_i - j] == pattern[mirror_i + 1 + j] for j in range(mirror_i + 1))
                            if search_over is not False:
                                horizontal_reflections.append(mirror_i + 1)
                            else:
                                continue
                        elif part == 2:
                            off_row = all_but_one(pattern[mirror_i - j] == pattern[mirror_i + 1 + j] for j in range(mirror_i + 1))
                            if off_row is not False:
                                index = list(range(mirror_i + 1))[off_row]
                                search_over = all_but_one(pattern[mirror_i - index][k] == pattern[mirror_i + 1 + index][k] for k in range(len(pattern[mirror_i + index])))
                                if search_over is not False:
                                    horizontal_reflections.append(mirror_i + 1)
                                else:
                                    continue
                            else:
                                continue

                if search_over is not False:
                    break

        if search_over is not False:
            continue

        # check columns
        pattern = list(zip(*pattern))  # transpose
        for i in range(len(pattern) - 1):
            # check for the edge case where the smudge is on the edge
            if part == 2:
                if all_but_one(pattern[i][j] == pattern[i+1][j] for j in range(len(pattern[i]))) is not False:
                    if i == 0:
                        vertical_reflections.append(1)
                        search_over = True
                    elif i == len(pattern) - 2:
                        vertical_reflections.append(len(pattern) - 1)
                        search_over = True
                    else:
                        reflection_axis = i + 0.5
                        # see if you're over the halfway point
                        if ceil(reflection_axis) > (len(pattern) - 1) / 2:
                            mirror_i = ceil(reflection_axis)
                            search_over = all_but_one(pattern[mirror_i - 1 - j] == pattern[mirror_i + j] for j in range(len(pattern) - mirror_i))
                            if search_over is not False:
                                vertical_reflections.append(mirror_i)
                            else:
                                continue
                        else:
                            mirror_i = floor(reflection_axis)
                            search_over = all_but_one(pattern[mirror_i - j] == pattern[mirror_i + 1 + j] for j in range(mirror_i + 1))
                            if search_over is not False:
                                vertical_reflections.append(mirror_i + 1)
                            else:
                                continue
                if search_over is not False:
                    break
            # check if it's the same as the one after
            if pattern[i] == pattern[i + 1]:
                # check for edge case where there is only one column to the left
                if i == 0 and part == 1:
                    vertical_reflections.append(1)
                    search_over = True
                else:
                    reflection_axis = i + 0.5
                    # see if you're over the halfway point
                    if ceil(reflection_axis) > (len(pattern) - 1) / 2:
                        mirror_i = ceil(reflection_axis)
                        if part == 1:
                            search_over = all(pattern[mirror_i - 1 - j] == pattern[mirror_i + j] for j in range(len(pattern) - mirror_i))
                            if search_over is not False:
                                vertical_reflections.append(mirror_i)
                            else:
                                continue
                        if part == 2:
                            off_col = all_but_one(pattern[mirror_i - 1 - j] == pattern[mirror_i + j] for j in range(len(pattern) - mirror_i))
                            if off_col is not False:
                                index = list(range(len(pattern) - mirror_i))[off_col]
                                search_over = all_but_one(pattern[mirror_i - 1 - index][k] == pattern[mirror_i + index][k] for k in range(len(pattern[mirror_i + index])))
                                if search_over is not False:
                                    vertical_reflections.append(mirror_i)
                                else:
                                    continue
                            else:
                                continue
                    else:
                        mirror_i = floor(reflection_axis)
                        if part == 1:
                            search_over = all(pattern[mirror_i - j] == pattern[mirror_i + 1 + j] for j in range(mirror_i + 1))
                            if search_over is not False:
                                vertical_reflections.append(mirror_i + 1)
                            else:
                                continue
                        elif part == 2:
                            off_col = all_but_one(pattern[mirror_i - j] == pattern[mirror_i + 1 + j] for j in range(mirror_i + 1))
                            if off_col is not False:
                                index = list(range(mirror_i + 1))[off_col]
                                search_over = all_but_one(pattern[mirror_i - index][k] == pattern[mirror_i + 1 + index][k] for k in range(len(pattern[mirror_i - index])))
                                if search_over is not False:
                                    vertical_reflections.append(mirror_i + 1)
                                else:
                                    continue
                            else:
                                continue

                if search_over is not False:
                    break

        if search_over is False:
            raise ValueError(f"No match found! Pattern {x}")
            
    return sum(vertical_reflections) + 100 * sum(horizontal_reflections)

# SOLUTIONS

# start_time = time.time()
# day13_part1 = find_mirror_summary('./inputs/day13.txt', 1)
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 13 - Part 1: {day13_part1}  {exec_time}ms")

# start_time = time.time()
# day13_part2 = find_mirror_summary('./inputs/day13.txt', 2)
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 13 - Part 2: {day13_part2}  {exec_time}ms")

#
# DAY 14 FUNCTIONS
#

# def find_rock_load(input_path: str) -> int:
#     """Given a"""
#     with open(input_path, newline='') as file:
#         rock_data = file.readlines()
    
#     rock_load = 0

#     return rock_load

# SOLUTIONS

#
# DAY 15 FUNCTIONS
#

def run_hash_algorithm(input_string: str) -> int:
    """Given a string, return the output of the HASH algorithm"""
    current_value = 0
    for char in input_string:
        # Determine the ASCII code for the current character of the string.
        # Increase the current value by the ASCII code you just determined.
        current_value += ord(char)
        # Set the current value to itself multiplied by 17.
        current_value = current_value * 17
        # Set the current value to the remainder of dividing itself by 256.
        current_value = current_value % 256

    return current_value

def find_hash_sum(initialization_sequence: str) -> int:
    """Given a sequence of steps, return the sum of results of a HASH algorithm."""
    steps = initialization_sequence.strip().split(",")
    hash_results = []
    for step in steps:
        hash_results.append(run_hash_algorithm(step))

    return sum(hash_results)

def find_focusing_power(initialization_sequence: str) -> int:
    """Given box and lens information, return the sum of the focusing power of each lens."""
    steps = initialization_sequence.strip().split(",")
    boxes = [{} for _ in range(256)]
    for step in steps:
        label = step.split("=")[0].split("-")[0]
        box = run_hash_algorithm(label)
        if "=" in step:
            value = step.split("=")[1]
            boxes[box][label] = value
        elif "-" in step:
            if label in boxes[box]:
                del boxes[box][label]
    
    focusing_power = 0
    for i, box in enumerate(boxes):
        boxes[i] = [(key, int(value)) for key, value in box.items()]
        for j, lens in enumerate(boxes[i]):
            focusing_power += (i + 1) * (j + 1) * lens[1]

    return focusing_power

# SOLUTIONS

# with open('./inputs/day15.txt',newline='') as file:
#     input_sequence = file.read().strip()
# start_time = time.time()
# day15_part1 = find_hash_sum(input_sequence)
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 15 - Part 1: {day15_part1}  {exec_time}ms")

# with open('./inputs/day15.txt',newline='') as file:
#     input_sequence = file.read().strip()
# start_time = time.time()
# day15_part2 = find_focusing_power(input_sequence)
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 15 - Part 2: {day15_part2}  {exec_time}ms")

#
# DAY 16 FUNCTIONS
#

def move(input_coord: tuple, direction: str) -> tuple:
    if direction == "right":
        return (input_coord[0], input_coord[1] + 1)
    if direction == "left":
        return (input_coord[0], input_coord[1] - 1)
    elif direction == "up":
        return (input_coord[0] - 1, input_coord[1])
    if direction == "down":
        return (input_coord[0] + 1, input_coord[1])

def find_energized_tiles(input_path: str, part: int = 1) -> int:
    """Given a map of splitters and mirrors, return the number of tiles containing beams."""
    with open(input_path, newline='') as file:
        cave_grid = [[i for i in line.strip()] for line in file.readlines()]
    
    def find_max_tile(beams):
        beam_grid = [[0 for _ in range(len(cave_grid[0]))] for _ in range(len(cave_grid))]
        dir_grid = [[set() for _ in range(len(cave_grid[0]))] for _ in range(len(cave_grid))]
        for beam in beams:
            while True:
                # break if you've hit an edge or you've already come at the next space from the same direction
                if (any(coord < 0 for coord in beam["coord"]) or
                    beam["coord"][0] > len(cave_grid) - 1 or
                    beam["coord"][1] > len(cave_grid[0]) - 1 or
                    beam["dir"] in dir_grid[beam["coord"][0]][beam["coord"][1]]
                ):
                    break
                beam_grid[beam["coord"][0]][beam["coord"][1]] += 1
                dir_grid[beam["coord"][0]][beam["coord"][1]].add(beam["dir"])
                if cave_grid[beam["coord"][0]][beam["coord"][1]] == '.':
                    next_beam = {
                        "coord": move(beam["coord"], beam["dir"]),
                        "dir": beam["dir"]
                    }
                elif cave_grid[beam["coord"][0]][beam["coord"][1]] == '\\':
                    if beam["dir"] == "right":
                        next_beam = {
                            "coord": move(beam["coord"], "down"),
                            "dir": "down"
                        }
                    elif beam["dir"] == "left":
                        next_beam = {
                            "coord": move(beam["coord"], "up"),
                            "dir": "up"
                        }
                    elif beam["dir"] == "up":
                        next_beam = {
                            "coord": move(beam["coord"], "left"),
                            "dir": "left"
                        }
                    elif beam["dir"] == "down":
                        next_beam = {
                            "coord": move(beam["coord"], "right"),
                            "dir": "right"
                        }
                elif cave_grid[beam["coord"][0]][beam["coord"][1]] == '/':
                    if beam["dir"] == "right":
                        next_beam = {
                            "coord": move(beam["coord"], "up"),
                            "dir": "up"
                        }
                    elif beam["dir"] == "left":
                        next_beam = {
                            "coord": move(beam["coord"], "down"),
                            "dir": "down"
                        }
                    elif beam["dir"] == "up":
                        next_beam = {
                            "coord": move(beam["coord"], "right"),
                            "dir": "right"
                        }
                    elif beam["dir"] == "down":
                        next_beam = {
                            "coord": move(beam["coord"], "left"),
                            "dir": "left"
                        }
                elif cave_grid[beam["coord"][0]][beam["coord"][1]] == '-':
                    if beam["dir"] == "right" or beam["dir"] == "left":
                        next_beam = {
                            "coord": move(beam["coord"], beam["dir"]),
                            "dir": beam["dir"]
                        }
                    elif beam["dir"] == "up" or beam["dir"] == "down":
                        # handle splitting
                        # pick a direction
                        next_beam = {
                            "coord": move(beam["coord"], "right"),
                            "dir": "right"
                        }
                        # append the other to the "beams" list
                        beams.append({
                            "coord": move(beam["coord"], "left"),
                            "dir": "left"
                        })
                elif cave_grid[beam["coord"][0]][beam["coord"][1]] == '|':
                    if beam["dir"] == "up" or beam["dir"] == "down":
                        next_beam = {
                            "coord": move(beam["coord"], beam["dir"]),
                            "dir": beam["dir"]
                        }
                    elif beam["dir"] == "right" or beam["dir"] == "left":
                        # handle splitting
                        # pick a direction
                        next_beam = {
                            "coord": move(beam["coord"], "up"),
                            "dir": "up"
                        }
                        # append the other to the "beams" list
                        beams.append({
                            "coord": move(beam["coord"], "down"),
                            "dir": "down"
                        })

                beam = next_beam
            
        return sum(1 for row in dir_grid for element in row if element != set())

    if part == 2:
        tiles = set()
        for i in range(len(cave_grid)):
            init_beam = {
                "coord": (i, 0),
                "dir": "right"
            }
            beams = [init_beam]
            tiles.add(find_max_tile(beams))
            init_beam = {
                "coord": (i, len(cave_grid[0]) - 1),
                "dir": "left"
            }
            beams = [init_beam]
            tiles.add(find_max_tile(beams))
        for j in range(len(cave_grid[0])):
            init_beam = {
                "coord": (0, j),
                "dir": "down"
            }
            beams = [init_beam]
            num_tiles = find_max_tile(beams)
            tiles.add(num_tiles) 
            init_beam = {
                "coord": (len(cave_grid) - 1, j),
                "dir": "up"
            }
            beams = [init_beam]
            tiles.add(find_max_tile(beams))
        return max(tiles)

    else:
        init_beam = {
            "coord": (0, 0),
            "dir": "right"
        }
        beams = [init_beam]
        return find_max_tile(beams)

# SOLUTIONS

# start_time = time.time()
# day16_part1 = find_energized_tiles('./inputs/day16.txt')
# exec_time = round(1000 * (time.time() - start_time), 4)
# print(f"Day 16 - Part 1: {day16_part1}  {exec_time}ms")

start_time = time.time()
day16_part2 = find_energized_tiles('./inputs/day16.txt', 2)
exec_time = round(1000 * (time.time() - start_time), 4)
print(f"Day 16 - Part 1: {day16_part2}  {exec_time}ms")

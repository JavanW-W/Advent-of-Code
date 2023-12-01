from config import DIGIT_STRINGS

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


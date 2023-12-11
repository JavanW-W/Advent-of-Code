DIGIT_STRINGS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

CARD_VALUES = {
    'A': 1,
    'K': 2,
    'Q': 3,
    'J': 4,
    'T': 5,
    '9': 6,
    '8': 7,
    '7': 8,
    '6': 9,
    '5': 10,
    '4': 11,
    '3': 12,
    '2': 13
}

PIPES = {
    "-": {"right": [0, 2, "right"], "left": [0, -2, "left"]},
    "|": {"up": [-2, 0, "up"], "down": [2, 0, "down"]},
    "L": {"down": [1, 1, "right"], "left": [-1, -1, "up"]},
    "J": {"down": [1, -1, "left"], "right": [-1, 1, "up"]},
    "F": {"up": [-1, 1, "right"], "left": [1, -1, "down"]},
    "7": {"right": [1, 1, "down"], "up": [-1, -1, "left"]},
    ".": {}
}
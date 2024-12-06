"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.day6_part1 = day6_part1;
exports.day6_part2 = day6_part2;
var fs = require("fs");
var directions = { "up": [-1, 0], "right": [0, 1], "down": [1, 0], "left": [0, -1] };
var turn_ninety_deg = { "up": "right", "right": "down", "down": "left", "left": "up" };
// Part 1
function day6_part1(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var mapped_area = input.split('\n');
    // find starting point
    var starting_point = mapped_area.join('').indexOf('^');
    var current_row = Math.floor(starting_point / mapped_area[0].length);
    var current_col = starting_point % mapped_area[0].length;
    var positions = ["".concat(current_row, ", ").concat(current_col)];
    var current_direction = "up";
    while (true) {
        var new_row = current_row + directions[current_direction][0];
        var new_col = current_col + directions[current_direction][1];
        if (new_row == mapped_area.length || new_col == mapped_area[0].length || new_row < 0 || new_col < 0) {
            break;
        }
        else {
            var new_pos = mapped_area[new_row][new_col];
            if (new_pos == '#') {
                current_direction = turn_ninety_deg[current_direction];
            }
            else {
                current_row = new_row;
                current_col = new_col;
                positions.push("".concat(current_row, ", ").concat(current_col));
            }
        }
    }
    return new Set(positions).size;
}
;
console.log("Part 1:", day6_part1('./inputs/day6.txt'));
// Part 2
function check_for_loop(mapped_area, init_positions, init_row, init_col, init_direction, obs_row, obs_col) {
    var current_row = init_row;
    var current_col = init_col;
    var current_direction = init_direction;
    var temp_positions = new Set(["".concat(init_row, ", ").concat(init_col, ", ").concat(init_direction)]);
    while (true) {
        var new_row = current_row + directions[current_direction][0];
        var new_col = current_col + directions[current_direction][1];
        if (new_row == mapped_area.length || new_col == mapped_area[0].length || new_row < 0 || new_col < 0) {
            return false;
        }
        else {
            var new_pos = mapped_area[new_row][new_col];
            if (new_pos == '#' || (new_row == obs_row && new_col == obs_col)) {
                current_direction = turn_ninety_deg[current_direction];
            }
            else {
                current_row = new_row;
                current_col = new_col;
            }
            if (init_positions.has("".concat(current_row, ", ").concat(current_col, ", ").concat(current_direction)) ||
                temp_positions.has("".concat(current_row, ", ").concat(current_col, ", ").concat(current_direction))) {
                return true;
            }
            temp_positions.add("".concat(current_row, ", ").concat(current_col, ", ").concat(current_direction));
        }
    }
}
function day6_part2(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var mapped_area = input.split('\n');
    // find starting point
    var starting_point = mapped_area.join('').indexOf('^');
    var current_row = Math.floor(starting_point / mapped_area[0].length);
    var current_col = starting_point % mapped_area[0].length;
    var starting_pos = "".concat(current_row, ", ").concat(current_col);
    var current_direction = "up";
    var positions = new Set(["".concat(current_row, ", ").concat(current_col, ", ").concat(current_direction)]);
    var obstacles = new Set();
    while (true) {
        var new_row = current_row + directions[current_direction][0];
        var new_col = current_col + directions[current_direction][1];
        if (new_row == mapped_area.length || new_col == mapped_area[0].length || new_row < 0 || new_col < 0) {
            break;
        }
        else {
            var new_pos = mapped_area[new_row][new_col];
            if (new_pos == '#') {
                current_direction = turn_ninety_deg[current_direction];
            }
            else {
                if (check_for_loop(mapped_area, positions, current_row, current_col, current_direction, new_row, new_col)) {
                    obstacles.add("".concat(new_row, ", ").concat(new_col));
                }
                current_row = new_row;
                current_col = new_col;
            }
            positions.add("".concat(current_row, ", ").concat(current_col, ", ").concat(current_direction));
        }
    }
    if (obstacles.has(starting_pos)) {
        return obstacles.size - 1;
    }
    return obstacles.size;
}
console.log("Part 2:", day6_part2('./inputs/day6.txt'));
// 1252 is too low
// 1644 is too high
// 1595 is not the right answer
// 1628 is not the right answer

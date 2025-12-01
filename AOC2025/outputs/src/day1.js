"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.day1_part1 = day1_part1;
exports.day1_part2 = day1_part2;
var fs = require("fs");
// Part 1
function day1_part1(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var rows = input.split(/\s+/);
    var position = 50;
    var count = 0;
    rows.forEach(function (row) {
        var dir = row.substring(0, 1);
        var clicks = parseInt(row.slice(1));
        if (dir == "R") {
            position = position + clicks;
        }
        else if (dir == "L") {
            position = position - clicks;
        }
        // handle wraparound
        while (position < 0 || position > 99) {
            if (position < 0) {
                position = 100 + position; // -1 => 99
            }
            else if (position > 99) {
                position = position - 100; // 100 => 0
            }
        }
        // count zeroes
        if (position == 0) {
            count += 1;
        }
    });
    return count;
}
console.log('Part 1:', day1_part1('./inputs/day1.txt'));
// Part 2
function day1_part2(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var rows = input.split(/\s+/);
    var position = 50;
    var count = 0;
    rows.forEach(function (row) {
        var dir = row.substring(0, 1);
        var clicks = parseInt(row.slice(1));
        var clicked = 0;
        // click one at a time
        while (clicked < clicks) {
            if (dir == "R") {
                position += 1;
            }
            else if (dir == "L") {
                position -= 1;
            }
            clicked += 1;
            // handle wraparound
            if (position == -1) {
                position = 99;
            }
            else if (position == 100) {
                position = 0;
            }
            // count zeroes
            if (position == 0) {
                count += 1;
            }
        }
    });
    return count;
}
console.log('Part 2:', day1_part2('./inputs/day1.txt'));

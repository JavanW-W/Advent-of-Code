"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.day3_part1 = day3_part1;
exports.day3_part2 = day3_part2;
var fs = require("fs");
// Part 1
function day3_part1(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var regex = /mul\(\d+,\d+\)/g;
    var muls = input.match(regex);
    var mul_total = 0;
    muls.forEach(function (instruction) {
        var just_nums = instruction.replace('mul(', '').replace(')', '');
        var to_multiply = just_nums.split(",");
        mul_total += parseInt(to_multiply[0]) * parseInt(to_multiply[1]);
    });
    return mul_total;
}
;
console.log('Part 1:', day3_part1('./inputs/day3.txt'));
// Part 2
function day3_part2(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var regex = /mul\(\d+,\d+\)|do\(\)|don't\(\)/g;
    var instructions = input.match(regex);
    var mul_total = 0;
    var enabled = true;
    instructions.forEach(function (instruction) {
        if (enabled == true) {
            if (instruction == "don't()") {
                enabled = false;
            }
            else if (instruction != "do()") {
                var just_nums = instruction.replace('mul(', '').replace(')', '');
                var to_multiply = just_nums.split(",");
                mul_total += parseInt(to_multiply[0]) * parseInt(to_multiply[1]);
            }
        }
        else {
            if (instruction == 'do()') {
                enabled = true;
            }
        }
    });
    return mul_total;
}
;
console.log('Part 2:', day3_part2('./inputs/day3.txt'));

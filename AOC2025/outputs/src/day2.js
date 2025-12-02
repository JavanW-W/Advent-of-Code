"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.day2_part1 = day2_part1;
var fs = require("fs");
// Part 1
function day2_part1(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var ranges = input.split(",");
    var invalid_ids = [];
    ranges.forEach(function (range) {
        var id = parseInt(range.split("-")[0]);
        var end = parseInt(range.split("-")[1]);
        while (id < end + 1) {
            // check if it's invalid
            var len = id.toString().length;
            if (len % 2 == 0) {
                if (id.toString().substring(0, len / 2) == id.toString().slice(len / 2)) {
                    invalid_ids.push(id);
                }
            }
            id += 1;
        }
    });
    var sum = invalid_ids.reduce(function (accumulator, current_id) { return accumulator + current_id; });
    return sum;
}
console.log('Part 1:', day2_part1('./inputs/day2.txt'));

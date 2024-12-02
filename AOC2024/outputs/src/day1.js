"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.day1_part1 = day1_part1;
exports.day1_part2 = day1_part2;
var fs = require("fs");
// Part 1
function day1_part1(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var flat_list = input.split(/\s+/);
    var left = [];
    var right = [];
    var distances = [];
    flat_list.forEach(function (value, index) {
        if (index % 2 === 0) {
            right.push(parseInt(value));
        }
        else {
            left.push(parseInt(value));
        }
    });
    left.sort(function (a, b) { return a - b; });
    right.sort(function (a, b) { return a - b; });
    left.forEach(function (value, index) {
        distances.push(Math.abs(value - right[index]));
    });
    var total_distance = distances.reduce(function (accumulator, currentValue) { return accumulator + currentValue; });
    return total_distance;
}
console.log('Part 1:', day1_part1('./inputs/day1.txt'));
function day1_part2(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var flat_list = input.split(/\s+/);
    var left = [];
    var right = [];
    var similarity = [];
    flat_list.forEach(function (value, index) {
        if (index % 2 === 0) {
            right.push(parseInt(value));
        }
        else {
            left.push(parseInt(value));
        }
    });
    left.forEach(function (value) {
        similarity.push(value * right.filter(function (x) { return x == value; }).length);
    });
    var total_similarity = similarity.reduce(function (accumulator, currentValue) { return accumulator + currentValue; });
    return total_similarity;
}
console.log('Part 2:', day1_part2('./inputs/day1.txt'));

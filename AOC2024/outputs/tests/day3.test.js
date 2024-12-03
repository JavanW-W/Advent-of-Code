"use strict";
// Part 1
Object.defineProperty(exports, "__esModule", { value: true });
var day3_1 = require("../src/day3");
describe('testing AoC 2024 Day 3 Part 1', function () {
    test('test case should give 161', function () {
        expect((0, day3_1.day3_part1)('./inputs/test/day3_part1.txt')).toBe(161);
    });
});
var day3_2 = require("../src/day3");
describe('testing AoC 2024 Day 3 Part 2', function () {
    test('test case should give 48', function () {
        expect((0, day3_2.day3_part2)('./inputs/test/day3_part2.txt')).toBe(48);
    });
});

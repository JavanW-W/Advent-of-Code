"use strict";
// Part 1
Object.defineProperty(exports, "__esModule", { value: true });
var day4_1 = require("../src/day4");
describe('testing AoC 2024 Day 4 Part 1', function () {
    test('test case should give 18', function () {
        expect((0, day4_1.day4_part1)('./inputs/test/day4.txt')).toBe(18);
    });
});
// Part 2
var day4_2 = require("../src/day4");
describe('testing AoC 2024 Day 4 Part 2', function () {
    test('test case should give 9', function () {
        expect((0, day4_2.day4_part2)('./inputs/test/day4.txt')).toBe(9);
    });
});

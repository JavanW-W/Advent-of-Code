"use strict";
// Part 1
Object.defineProperty(exports, "__esModule", { value: true });
var day2_1 = require("../src/day2");
describe('testing AoC 2024 Day 2 Part 1', function () {
    test('test case should give 2', function () {
        expect((0, day2_1.day2_part1)('./inputs/test/day2.txt')).toBe(2);
    });
});
// Part 2
var day2_2 = require("../src/day2");
describe('testing AoC 2024 Day 2 Part 2', function () {
    test('test case should give 4', function () {
        expect((0, day2_2.day2_part2)('./inputs/test/day2.txt')).toBe(4);
    });
});

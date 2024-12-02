"use strict";
// Part 1
Object.defineProperty(exports, "__esModule", { value: true });
var day1_1 = require("../src/day1");
describe('testing AoC 2024 Day 1 Part 1', function () {
    test('test case should give 11', function () {
        expect((0, day1_1.day1_part1)('./inputs/test/day1.txt')).toBe(11);
    });
});
var day1_2 = require("../src/day1");
describe('testing AoC 2024 Day 1 Part 2', function () {
    test('test case should give 31', function () {
        expect((0, day1_2.day1_part2)('./inputs/test/day1.txt')).toBe(31);
    });
});

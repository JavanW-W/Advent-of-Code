"use strict";
// Part 1
Object.defineProperty(exports, "__esModule", { value: true });
var day6_1 = require("../src/day6");
describe('testing AoC 2024 Day 6 Part 1', function () {
    test('test case should give 41', function () {
        expect((0, day6_1.day6_part1)('./inputs/test/day6.txt')).toBe(41);
    });
});
// Part 2
var day6_2 = require("../src/day6");
describe('testing AoC 2024 Day 6 Part 2', function () {
    test('test case should give 6', function () {
        expect((0, day6_2.day6_part2)('./inputs/test/day6.txt')).toBe(6);
    });
});

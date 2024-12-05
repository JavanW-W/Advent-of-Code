"use strict";
// Part 1
Object.defineProperty(exports, "__esModule", { value: true });
var day5_1 = require("../src/day5");
describe('testing AoC 2024 Day 5 Part 1', function () {
    test('test case should give 143', function () {
        expect((0, day5_1.day5_part1)('./inputs/test/day5.txt')).toBe(143);
    });
});
// Part 2
var day5_2 = require("../src/day5");
describe('testing AoC 2024 Day 5 Part 2', function () {
    test('test case should give 123', function () {
        expect((0, day5_2.day5_part2)('./inputs/test/day5.txt')).toBe(123);
    });
});

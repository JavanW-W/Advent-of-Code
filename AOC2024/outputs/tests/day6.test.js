"use strict";
// Part 1
Object.defineProperty(exports, "__esModule", { value: true });
const day6_1 = require("../src/day6");
describe('testing AoC 2024 Day 6 Part 1', () => {
    test('test case should give 41', () => {
        expect((0, day6_1.day6_part1)('./inputs/test/day6.txt')).toBe(41);
    });
});
// Part 2
const day6_2 = require("../src/day6");
describe('testing AoC 2024 Day 6 Part 2', () => {
    test('test case should give 6', () => {
        expect((0, day6_2.day6_part2)('./inputs/test/day6.txt')).toBe(6);
    });
});

// Part 1

import { day4_part1 } from '../src/day4';

describe('testing AoC 2024 Day 4 Part 1', () => {
  test('test case should give 18', () => {
    expect(day4_part1('./inputs/test/day4.txt')).toBe(18);
  });
});

// Part 2

import { day4_part2 } from '../src/day4';

describe('testing AoC 2024 Day 4 Part 2', () => {
  test('test case should give 9', () => {
    expect(day4_part2('./inputs/test/day4.txt')).toBe(9);
  });
});
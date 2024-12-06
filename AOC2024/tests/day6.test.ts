// Part 1

import { day6_part1 } from '../src/day6';

describe('testing AoC 2024 Day 6 Part 1', () => {
  test('test case should give 41', () => {
    expect(day6_part1('./inputs/test/day6.txt')).toBe(41);
  });
});

// Part 2

import { day6_part2 } from '../src/day6';

describe('testing AoC 2024 Day 6 Part 2', () => {
  test('test case should give 6', () => {
    expect(day6_part2('./inputs/test/day6.txt')).toBe(6);
  });
});
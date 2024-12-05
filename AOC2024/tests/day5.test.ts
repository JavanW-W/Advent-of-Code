// Part 1

import { day5_part1 } from '../src/day5';

describe('testing AoC 2024 Day 5 Part 1', () => {
  test('test case should give 143', () => {
    expect(day5_part1('./inputs/test/day5.txt')).toBe(143);
  });
});

// Part 2

import { day5_part2 } from '../src/day5';

describe('testing AoC 2024 Day 5 Part 2', () => {
  test('test case should give 123', () => {
    expect(day5_part2('./inputs/test/day5.txt')).toBe(123);
  });
});
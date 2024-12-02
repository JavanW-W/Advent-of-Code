// Part 1

import { day1_part1 } from '../src/day1';

describe('testing AoC 2024 Day 1 Part 1', () => {
  test('test case should give 11', () => {
    expect(day1_part1('./inputs/test/day1.txt')).toBe(11);
  });
});

import { day1_part2 } from '../src/day1';

describe('testing AoC 2024 Day 1 Part 2', () => {
  test('test case should give 31', () => {
    expect(day1_part2('./inputs/test/day1.txt')).toBe(31);
  });
});

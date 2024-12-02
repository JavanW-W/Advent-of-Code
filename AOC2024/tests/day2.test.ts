// Part 1

import { day2_part1 } from '../src/day2';

describe('testing AoC 2024 Day 2 Part 1', () => {
  test('test case should give 2', () => {
    expect(day2_part1('./inputs/test/day2.txt')).toBe(2);
  });
});

// Part 2

import { day2_part2 } from '../src/day2';

describe('testing AoC 2024 Day 2 Part 2', () => {
  test('test case should give 4', () => {
    expect(day2_part2('./inputs/test/day2.txt')).toBe(4);
  });
});

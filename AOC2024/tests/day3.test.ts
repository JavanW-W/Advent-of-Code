// Part 1

import { day3_part1 } from '../src/day3';

describe('testing AoC 2024 Day 3 Part 1', () => {
  test('test case should give 161', () => {
    expect(day3_part1('./inputs/test/day3_part1.txt')).toBe(161);
  });
});

//Part 2

import { day3_part2 } from '../src/day3';

describe('testing AoC 2024 Day 3 Part 2', () => {
  test('test case should give 48', () => {
    expect(day3_part2('./inputs/test/day3_part2.txt')).toBe(48);
  });
});
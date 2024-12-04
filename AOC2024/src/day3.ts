import * as fs from 'fs';

// Part 1
export function day3_part1(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    const regex = /mul\(\d+,\d+\)/g;
    let muls = input.match(regex);
    let mul_total = 0
    muls.forEach(instruction => {
        let just_nums = instruction.replace('mul(', '').replace(')', '')
        let to_multiply = just_nums.split(",")
        mul_total += parseInt(to_multiply[0]) * parseInt(to_multiply[1])
    });
    
    return mul_total;
};

console.log('Part 1:', day3_part1('./inputs/day3.txt'));

// Part 2
export function day3_part2(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    const regex = /mul\(\d+,\d+\)|do\(\)|don't\(\)/g;
    let instructions = input.match(regex);
    let mul_total = 0
    let enabled = true
    instructions.forEach(instruction => {
        if (enabled == true) {
            if (instruction == "don't()") {
                enabled = false
            } else if (instruction != "do()") {
                let just_nums = instruction.replace('mul(', '').replace(')', '')
                let to_multiply = just_nums.split(",")
                mul_total += parseInt(to_multiply[0]) * parseInt(to_multiply[1])
            }
        } else {
            if (instruction == 'do()') {
                enabled = true
            }
        }
    });
    
    return mul_total;
};

console.log('Part 2:', day3_part2('./inputs/day3.txt'));
import * as fs from 'fs';

// Part 1
export function day7_part1(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let equations = input.split('\n')
    equations.forEach(equation => {
        let test_val = parseInt(equation.split(": ")[0])
        let nums = equation.split(": ")[1].split(" ").map(a => parseInt(a))

    });

    return 3749;
};

// console.log("Part 1:", day7_part1('./inputs/day7.txt'))

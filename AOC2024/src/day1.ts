import * as fs from 'fs';

// Part 1
export function day1_part1(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let flat_list = input.split(/\s+/);
    let left: number[] = [];
    let right: number[] = [];
    let distances: number[] = [];
    flat_list.forEach((value, index) => {
        if (index % 2 === 0) {
            right.push(parseInt(value));
        } else {
            left.push(parseInt(value));
        }
    });
    left.sort((a, b) => a - b);
    right.sort((a, b) => a - b);
    
    left.forEach((value, index) => {
        distances.push(Math.abs(value - right[index]))
    });

    let total_distance = distances.reduce((accumulator, currentValue) => accumulator + currentValue)

    return total_distance
}

console.log('Part 1:', day1_part1('./inputs/day1.txt'));

export function day1_part2(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let flat_list = input.split(/\s+/);
    let left: number[] = [];
    let right: number[] = [];
    let similarity: number[] = [];
    flat_list.forEach((value, index) => {
        if (index % 2 === 0) {
            right.push(parseInt(value));
        } else {
            left.push(parseInt(value));
        }
    });
    
    left.forEach(value => {
        similarity.push(value * right.filter(x => x==value).length)
    });

    let total_similarity = similarity.reduce((accumulator, currentValue) => accumulator + currentValue)

    return total_similarity
}

console.log('Part 2:', day1_part2('./inputs/day1.txt'));
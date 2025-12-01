import * as fs from 'fs';

// Part 1
export function day1_part1(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let rows = input.split(/\s+/);
    let position: number = 50;
    let count: number = 0;
    rows.forEach((row) => {
        let dir: string = row.substring(0,1)
        let clicks: number = parseInt(row.slice(1))
        if (dir == "R") {
            position = position + clicks
        } else if (dir == "L") {
            position = position - clicks
        }

        // handle wraparound
        if (position < 0) {
            position = 100 + position // -1 => 99
        } else if (position > 99) {
            position = position - 100 // 100 => 0
        }

        // count zeroes
        if (position == 0) {
            count += 1
        }
    })

    return count
}

console.log('Part 1:', day1_part1('./inputs/day1.txt'));

// Part 2

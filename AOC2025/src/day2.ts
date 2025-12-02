import * as fs from 'fs';

// Part 1
export function day2_part1(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let ranges: string[] = input.split(",");
    let invalid_ids: number[] = []
    ranges.forEach((range) => {
        let id: number = parseInt(range.split("-")[0])
        let end: number = parseInt(range.split("-")[1])
        while(id < end + 1) {
            // check if it's invalid
            let len: number = id.toString().length
            if (len%2 == 0) {
                if (id.toString().substring(0, len/2) == id.toString().slice(len/2)) {
                    invalid_ids.push(id)
                }
            }
            id += 1
        }
    })

    let sum: number = invalid_ids.reduce(
        (accumulator, current_id) => accumulator + current_id
    )
    return sum
}

console.log('Part 1:', day2_part1('./inputs/day2.txt'));

import * as fs from 'fs';

const directions = {"up": [-1, 0], "right": [0, 1], "down": [1, 0], "left": [0, -1]}
const turn_ninety_deg = {"up": "right", "right": "down", "down": "left", "left": "up"}

// Part 1
export function day6_part1(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let mapped_area = input.split('\n')
    // find starting point
    let starting_point = mapped_area.join('').indexOf('^')
    let current_row = Math.floor(starting_point / mapped_area[0].length)
    let current_col = starting_point % mapped_area[0].length
    let positions: string[] = [`${current_row}, ${current_col}`]
    let current_direction = "up"
    while (true) {
        let new_row = current_row + directions[current_direction][0]
        let new_col = current_col + directions[current_direction][1]
        if (new_row == mapped_area.length || new_col == mapped_area[0].length || new_row < 0 || new_col < 0) {
            break;
        } else {
            let new_pos = mapped_area[new_row][new_col]
            if (new_pos == '#') {
                current_direction = turn_ninety_deg[current_direction]
            } else {
                current_row = new_row
                current_col = new_col
                positions.push(`${current_row}, ${current_col}`)
            }    
        }
    }

    return new Set(positions).size;
};

console.log("Part 1:", day6_part1('./inputs/day6.txt'))

// Part 2

function check_for_loop(mapped_area: string[], init_positions: Set<string>, init_row: number, init_col: number, init_direction: string, obs_row: number, obs_col: number): boolean {
    var current_row = init_row
    var current_col = init_col
    var current_direction = init_direction
    var temp_positions = new Set([`${init_row}, ${init_col}, ${init_direction}`])
    while (true) {
        var new_row = current_row + directions[current_direction][0]
        var new_col = current_col + directions[current_direction][1]
        if (new_row == mapped_area.length || new_col == mapped_area[0].length || new_row < 0 || new_col < 0) {
            return false;
        } else {
            let new_pos = mapped_area[new_row][new_col]
            if (new_pos == '#' || (new_row == obs_row && new_col == obs_col)) {
                current_direction = turn_ninety_deg[current_direction]
            } else {
                current_row = new_row
                current_col = new_col
            }
            if (init_positions.has(`${current_row}, ${current_col}, ${current_direction}`) ||
            temp_positions.has(`${current_row}, ${current_col}, ${current_direction}`)) {
                return true;
            }
            temp_positions.add(`${current_row}, ${current_col}, ${current_direction}`)
        }
    }
}

export function day6_part2(file_path: string): number {
    const input = fs.readFileSync(file_path, 'utf8');
    const mapped_area = input.split('\n')
    // find starting point
    const starting_point = mapped_area.join('').indexOf('^')
    var current_row = Math.floor(starting_point / mapped_area[0].length)
    var current_col = starting_point % mapped_area[0].length
    const starting_pos = `${current_row}, ${current_col}`
    var current_direction = "up"
    var positions = new Set<string>([`${current_row}, ${current_col}, ${current_direction}`])
    var obstacles = new Set<string>()
    while (true) {
        var new_row = current_row + directions[current_direction][0]
        var new_col = current_col + directions[current_direction][1]
        if (new_row == mapped_area.length || new_col == mapped_area[0].length || new_row < 0 || new_col < 0) {
            break;
        } else {
            var new_pos = mapped_area[new_row][new_col]
            if (new_pos == '#') {
                current_direction = turn_ninety_deg[current_direction]
            } else {
                if (check_for_loop(mapped_area, positions, current_row, current_col, current_direction, new_row, new_col)) {
                    obstacles.add(`${new_row}, ${new_col}`)
                }
                current_row = new_row
                current_col = new_col
            }
            positions.add(`${current_row}, ${current_col}, ${current_direction}`)
        }
    }

    if (obstacles.has(starting_pos)) {
        return obstacles.size - 1
    }
    return obstacles.size;
}

console.log("Part 2:", day6_part2('./inputs/day6.txt'))
// 1252 is too low
// 1644 is too high
// 1595 is not the right answer
// 1628 is not the right answer
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

function get_positions(file_path: string): Set<string> {
    let input = fs.readFileSync(file_path, 'utf8');
    let mapped_area = input.split('\n')
    // find starting point
    let starting_point = mapped_area.join('').indexOf('^')
    let current_row = Math.floor(starting_point / mapped_area[0].length)
    let current_col = starting_point % mapped_area[0].length
    let positions: Set<string> = new Set([`${current_row}, ${current_col}`])
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
                positions.add(`${current_row}, ${current_col}`)
            }    
        }
    }

    return new Set(positions);
};

export function day6_part2(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let mapped_area = input.split('\n')
    // find starting point
    const starting_point = mapped_area.join('').indexOf('^')
    const init_row = Math.floor(starting_point / mapped_area[0].length)
    const init_col = starting_point % mapped_area[0].length
    const init_direction = "up"    
    const init_pos = `${init_row}, ${init_col}`
    let obstacles: Set<string> = new Set<string>()
    let positions = get_positions(file_path)
    for (const position of positions) {
        let current_row = init_row
        let current_col = init_col
        let current_direction = init_direction
        let obs_row = parseInt(position.split(',')[0])
        let obs_col = parseInt(position.split(',')[1])
        let temp_positions = new Set([`${current_row}, ${current_col}, ${current_direction}`])
        while (true) {
            let new_row = current_row + directions[current_direction][0]
            let new_col = current_col + directions[current_direction][1]
            if (new_row == mapped_area.length || new_col == mapped_area[0].length || new_row < 0 || new_col < 0) {
                break;
            } else {
                let new_pos = mapped_area[new_row][new_col]
                if (new_pos == '#' || (new_row == obs_row && new_col == obs_col)) {
                    current_direction = turn_ninety_deg[current_direction]
                } else {
                    current_row = new_row
                    current_col = new_col
                }
                if (temp_positions.has(`${current_row}, ${current_col}, ${current_direction}`)) {
                    obstacles.add(position)
                    break;
                }
                temp_positions.add(`${current_row}, ${current_col}, ${current_direction}`)
            }
        }    
    }

    if (obstacles.has(init_pos)) {
        return obstacles.size - 1
    }
    return obstacles.size
}

console.log("Part 2:", day6_part2('./inputs/day6.txt'))

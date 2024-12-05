import * as fs from 'fs';

// Part 1
export function day5_part1(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let rules = input.split('\n\n')[0].split('\n')
    let updates = input.split('\n\n')[1].split('\n')
    let sum: number = 0
    let correct: number = 0
    for (let update of updates) {
        let broken = false
        let list = update.split(',')
        pageloop: for (let i = 0; i < list.length; i++) {
            let page = list[i]
            // get matching rules
            if (i > 0) {
                let before_rules = rules.filter(a => a.startsWith(page))
                before_rules.forEach(rule => {
                    let later_page = rule.split('|')[1]
                    beforeloop: for (let j = i; j >= 0; j--) {
                        if (list[j] == later_page) {
                            broken = true;
                            return;
                        };
                    };
                });
            };
            if (i < list.length - 1) {
                let after_rules = rules.filter(a => a.endsWith(page))
                after_rules.forEach(rule => {
                    let former_page = rule.split('|')[0]
                    afterloop: for (let j = i + 1; j < list.length; j++) {
                        if (list[j] == former_page) {
                            broken = true;
                            return;
                        };
                    };
                });    
            };
        };
        if (!broken) {
            correct++
            sum += parseInt(list[(list.length - 1) / 2]) 
        }
    };

    return sum;
};

console.log('Part 1:', day5_part1('./inputs/day5.txt'));

// Part 2
export function day5_part2(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let rules = input.split('\n\n')[0].split('\n')
    let updates = input.split('\n\n')[1].split('\n')
    let sum: number = 0
    for (let update of updates) {
        let reordered = false
        let list = update.split(',')
        list.sort((b, a) => {
            let after_rules = rules.filter(c => c.endsWith(a))
            let match = false
            after_rules.forEach(rule => {
                let former_page = rule.split('|')[0]
                if (b == former_page) {
                    match = true
                };
            });
            if (match) {
                reordered = true
                return -1
            }
                return 0
        });
        if (reordered) {
            sum += parseInt(list[(list.length - 1) / 2]) 
        }
    };

    return sum;
}

console.log('Part 2:', day5_part2('./inputs/day5.txt'));

import * as fs from 'fs';

// Part 1
function valid_report(report: string[]): boolean {
    let diffs: number[] = []
    for (let i = 1; i < report.length; i++) {
        let diff = parseInt(report[i]) - parseInt(report[i - 1]);
        if (diff == 0 || diff > 3 || diff < -3) {
            return false;
        };
        diffs.push(diff);
    };
    let all_positive = diffs.filter(function(a) { return (a > 0); })
    let all_negative = diffs.filter(function(a) { return (a < 0); })

    return (diffs.length == all_positive.length) || (diffs.length == all_negative.length);
};

export function day2_part1(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let reports = input.split('\n');
    let total_safe = 0
    reports.forEach(raw_report => {
        let report = raw_report.split(' ');
        if (valid_report(report)) {
            ++total_safe
        };
    });

    return total_safe;
};

console.log('Part 1:', day2_part1('./inputs/day2.txt'));

// Part 2

export function day2_part2(file_path: string): number {
    let input = fs.readFileSync(file_path, 'utf8');
    let reports = input.split('\n');
    let total_safe = 0
    reports.forEach(raw_report => {
        let report = raw_report.split(' ');
        if (valid_report(report)) {
            ++total_safe
        } else {
            for (let i = 0; i < report.length; i++) {
                let filtered_report = report.filter((_, index) => index !== i);
                if (valid_report(filtered_report)) {
                    ++total_safe
                    break;
                };
            }
        }
    });

    return total_safe;
};

console.log('Part 2:', day2_part2('./inputs/day2.txt'));
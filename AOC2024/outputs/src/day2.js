"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.day2_part1 = day2_part1;
exports.day2_part2 = day2_part2;
var fs = require("fs");
// Part 1
function valid_report(report) {
    var diffs = [];
    for (var i = 1; i < report.length; i++) {
        var diff = parseInt(report[i]) - parseInt(report[i - 1]);
        if (diff == 0 || diff > 3 || diff < -3) {
            return false;
        }
        ;
        diffs.push(diff);
    }
    ;
    var all_positive = diffs.filter(function (a) { return (a > 0); });
    var all_negative = diffs.filter(function (a) { return (a < 0); });
    return (diffs.length == all_positive.length) || (diffs.length == all_negative.length);
}
;
function day2_part1(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var reports = input.split('\n');
    var total_safe = 0;
    reports.forEach(function (raw_report) {
        var report = raw_report.split(' ');
        if (valid_report(report)) {
            ++total_safe;
        }
        ;
    });
    return total_safe;
}
;
console.log('Part 1:', day2_part1('./inputs/day2.txt'));
// Part 2
function day2_part2(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var reports = input.split('\n');
    var total_safe = 0;
    reports.forEach(function (raw_report) {
        var report = raw_report.split(' ');
        if (valid_report(report)) {
            ++total_safe;
        }
        else {
            var _loop_1 = function (i) {
                var filtered_report = report.filter(function (_, index) { return index !== i; });
                if (valid_report(filtered_report)) {
                    ++total_safe;
                    return "break";
                }
                ;
            };
            for (var i = 0; i < report.length; i++) {
                var state_1 = _loop_1(i);
                if (state_1 === "break")
                    break;
            }
        }
    });
    return total_safe;
}
;
console.log('Part 2:', day2_part2('./inputs/day2.txt'));

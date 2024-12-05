"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.day5_part1 = day5_part1;
exports.day5_part2 = day5_part2;
var fs = require("fs");
// Part 1
function day5_part1(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var rules = input.split('\n\n')[0].split('\n');
    var updates = input.split('\n\n')[1].split('\n');
    var sum = 0;
    var correct = 0;
    var _loop_1 = function (update) {
        var broken = false;
        var list = update.split(',');
        var _loop_2 = function (i) {
            var page = list[i];
            // get matching rules
            if (i > 0) {
                var before_rules = rules.filter(function (a) { return a.startsWith(page); });
                before_rules.forEach(function (rule) {
                    var later_page = rule.split('|')[1];
                    beforeloop: for (var j = i; j >= 0; j--) {
                        if (list[j] == later_page) {
                            broken = true;
                            return;
                        }
                        ;
                    }
                    ;
                });
            }
            ;
            if (i < list.length - 1) {
                var after_rules = rules.filter(function (a) { return a.endsWith(page); });
                after_rules.forEach(function (rule) {
                    var former_page = rule.split('|')[0];
                    afterloop: for (var j = i + 1; j < list.length; j++) {
                        if (list[j] == former_page) {
                            broken = true;
                            return;
                        }
                        ;
                    }
                    ;
                });
            }
            ;
        };
        pageloop: for (var i = 0; i < list.length; i++) {
            _loop_2(i);
        }
        ;
        if (!broken) {
            correct++;
            sum += parseInt(list[(list.length - 1) / 2]);
        }
    };
    for (var _i = 0, updates_1 = updates; _i < updates_1.length; _i++) {
        var update = updates_1[_i];
        _loop_1(update);
    }
    ;
    return sum;
}
;
console.log('Part 1:', day5_part1('./inputs/day5.txt'));
// Part 2
function day5_part2(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var rules = input.split('\n\n')[0].split('\n');
    var updates = input.split('\n\n')[1].split('\n');
    var sum = 0;
    var _loop_3 = function (update) {
        var reordered = false;
        var list = update.split(',');
        list.sort(function (b, a) {
            var after_rules = rules.filter(function (c) { return c.endsWith(a); });
            var match = false;
            after_rules.forEach(function (rule) {
                var former_page = rule.split('|')[0];
                if (b == former_page) {
                    match = true;
                }
                ;
            });
            if (match) {
                reordered = true;
                return -1;
            }
            return 0;
        });
        if (reordered) {
            sum += parseInt(list[(list.length - 1) / 2]);
        }
    };
    for (var _i = 0, updates_2 = updates; _i < updates_2.length; _i++) {
        var update = updates_2[_i];
        _loop_3(update);
    }
    ;
    return sum;
}
console.log('Part 2:', day5_part2('./inputs/day5.txt'));

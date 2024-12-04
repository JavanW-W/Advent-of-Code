"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.day4_part1 = day4_part1;
exports.day4_part2 = day4_part2;
var fs = require("fs");
// Part 1
function day4_part1(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var rows = input.split('\n');
    var matches = 0;
    // check for diagonal matches
    for (var i = 0; i < rows.length; i++) {
        for (var j = 0; j < rows[i].length; j++) {
            if (rows[i][j] == 'X') {
                if (j > 2) { //left
                    if (rows[i][j - 1] == 'M') {
                        if (rows[i][j - 2] == 'A') {
                            if (rows[i][j - 3] == 'S') {
                                matches++;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                }
                ;
                if (j < rows[i].length - 3) { //right
                    if (rows[i][j + 1] == 'M') {
                        if (rows[i][j + 2] == 'A') {
                            if (rows[i][j + 3] == 'S') {
                                matches++;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                }
                ;
                if (i > 2) { //up
                    if (rows[i - 1][j] == 'M') {
                        if (rows[i - 2][j] == 'A') {
                            if (rows[i - 3][j] == 'S') {
                                matches++;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                }
                ;
                if (i < rows.length - 3) { //down
                    if (rows[i + 1][j] == 'M') {
                        if (rows[i + 2][j] == 'A') {
                            if (rows[i + 3][j] == 'S') {
                                matches++;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                }
                ;
                if (i > 2 && j > 2) { //up-left
                    if (rows[i - 1][j - 1] == 'M') {
                        if (rows[i - 2][j - 2] == 'A') {
                            if (rows[i - 3][j - 3] == 'S') {
                                matches++;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                }
                ;
                if (i > 2 && j < rows[i].length - 3) { //up-right
                    if (rows[i - 1][j + 1] == 'M') {
                        if (rows[i - 2][j + 2] == 'A') {
                            if (rows[i - 3][j + 3] == 'S') {
                                matches++;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                }
                ;
                if (i < rows.length - 3 && j > 2) { //down-left
                    if (rows[i + 1][j - 1] == 'M') {
                        if (rows[i + 2][j - 2] == 'A') {
                            if (rows[i + 3][j - 3] == 'S') {
                                matches++;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                }
                ;
                if (i < rows.length - 3 && j < rows[i].length - 3) { //down-right
                    if (rows[i + 1][j + 1] == 'M') {
                        if (rows[i + 2][j + 2] == 'A') {
                            if (rows[i + 3][j + 3] == 'S') {
                                matches++;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                }
                ;
            }
            ;
        }
        ;
    }
    ;
    return matches;
}
;
console.log('Part 1:', day4_part1('./inputs/day4.txt'));
// Part 2
function day4_part2(file_path) {
    var input = fs.readFileSync(file_path, 'utf8');
    var rows = input.split('\n');
    var matches = 0;
    // check for diagonal matches
    for (var i = 1; i < rows.length - 1; i++) {
        for (var j = 1; j < rows[i].length - 1; j++) {
            if (rows[i][j] == 'A') {
                if (rows[i - 1][j - 1] == 'M' && rows[i + 1][j + 1] == 'S') {
                    if (rows[i - 1][j + 1] == 'M' && rows[i + 1][j - 1] == 'S' ||
                        rows[i - 1][j + 1] == 'S' && rows[i + 1][j - 1] == 'M') {
                        matches++;
                    }
                }
                else if (rows[i - 1][j - 1] == 'S' && rows[i + 1][j + 1] == 'M') {
                    if (rows[i - 1][j + 1] == 'M' && rows[i + 1][j - 1] == 'S' ||
                        rows[i - 1][j + 1] == 'S' && rows[i + 1][j - 1] == 'M') {
                        matches++;
                    }
                }
                ;
            }
            ;
        }
        ;
    }
    ;
    return matches;
}
;
console.log('Part 2:', day4_part2('./inputs/day4.txt'));

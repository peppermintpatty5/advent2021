#!/usr/bin/env python3

import sys


def fold_horizontal(dots: set, x_line: int) -> set:
    return {(x, y) if x < x_line else (x_line - (x - x_line), y) for x, y in dots}


def fold_vertical(dots: set, y_line: int) -> set:
    return {(x, y) if y < y_line else (x, y_line - (y - y_line)) for x, y in dots}


def part1(input_txt: str) -> int:
    top_txt, bottom_txt = input_txt.split("\n\n")
    dots = {tuple(map(int, line.split(","))) for line in top_txt.splitlines()}
    folds = [(line[11], int(line[13:])) for line in bottom_txt.splitlines()]

    for f, n in folds[:1]:
        dots = fold_horizontal(dots, n) if f == "x" else fold_vertical(dots, n)

    return len(fold_horizontal(dots, 655))


def part2(input_txt: str) -> str:
    top_txt, bottom_txt = input_txt.split("\n\n")
    dots = {tuple(map(int, line.split(","))) for line in top_txt.splitlines()}
    folds = [(line[11], int(line[13:])) for line in bottom_txt.splitlines()]

    for f, n in folds:
        dots = fold_horizontal(dots, n) if f == "x" else fold_vertical(dots, n)
    max_x, max_y = max(dots)

    return "\n".join(
        "".join("#" if (x, y) in dots else " " for x in range(max_x + 1))
        for y in range(max_y + 1)
    )


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys


def part1(input_txt: str) -> int:
    h_pos = depth = 0
    for line in input_txt.splitlines():
        com, x = line.split()
        x = int(x)
        if com == "down":
            depth += x
        if com == "up":
            depth -= x
        if com == "forward":
            h_pos += x

    return h_pos * depth


def part2(input_txt: str) -> int:
    aim = h_pos = depth = 0
    for line in input_txt.splitlines():
        com, x = line.split()
        x = int(x)
        if com == "down":
            aim += x
        if com == "up":
            aim -= x
        if com == "forward":
            h_pos += x
            depth += aim * x

    return h_pos * depth


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys


def part1(input_txt: str) -> int:
    pos = list(map(int, input_txt.split(",")))

    return min(sum(abs(x - i) for x in pos) for i in range(max(pos)))


def part2(input_txt: str) -> int:
    pos = list(map(int, input_txt.split(",")))

    return min(
        sum(abs(x - i) * (abs(x - i) + 1) // 2 for x in pos) for i in range(max(pos))
    )


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

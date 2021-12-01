#!/usr/bin/env python3

import sys


def part1(input_txt: str) -> int:
    x = 0
    nums = [int(i) for i in input_txt.splitlines()]
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            x += 1
    return x


def part2(input_txt: str) -> int:
    x = 0
    nums = [int(i) for i in input_txt.splitlines()]
    for i in range(len(nums) - 3):
        if nums[i] < nums[i + 3]:
            x += 1
    return x


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

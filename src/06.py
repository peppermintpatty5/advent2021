#!/usr/bin/env python3

import sys


def part1(input_txt: str) -> int:
    fish = list(map(int, input_txt.split(",")))

    for _ in range(80):
        n = len(fish)
        for i in range(n):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1

    return len(fish)


def part2(input_txt: str) -> int:
    fish = list(map(int, input_txt.split(",")))
    fish_tank = [fish.count(i) for i in range(9)]

    for _ in range(256):
        x = fish_tank[0]
        for i in range(1, 9):
            fish_tank[i - 1] = fish_tank[i]
        fish_tank[6] += x
        fish_tank[8] = x

    return sum(fish_tank)


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

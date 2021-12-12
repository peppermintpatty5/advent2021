#!/usr/bin/env python3

import sys
from itertools import product
from typing import List, Tuple


def adj(r: int, c: int) -> List[Tuple[int, int]]:
    """
    Return the in-bounds points adjacent to `(r, c)`.
    """
    return [
        (r0, c0)
        for r0, c0 in product({r - 1, r, r + 1}, {c - 1, c, c + 1})
        if 0 <= r0 < 10 and 0 <= c0 < 10 and (r0, c0) != (r, c)
    ]


def do_step(grid: list) -> int:
    """
    Advance grid by a single step and return the number of flashes.
    """
    flashed = set()

    for r in range(10):
        for c in range(10):
            grid[r][c] += 1

    while True:
        new_flashed = {
            (r, c)
            for r, c in product(range(10), range(10))
            if grid[r][c] >= 10 and (r, c) not in flashed
        }

        if new_flashed:
            for r, c in new_flashed:
                for (r0, c0) in adj(r, c):
                    grid[r0][c0] += 1
            flashed |= new_flashed
        else:
            for r in range(10):
                for c in range(10):
                    if grid[r][c] >= 10:
                        grid[r][c] = 0
            return len(flashed)


def part1(input_txt: str) -> int:
    grid = [[int(x) for x in line] for line in input_txt.splitlines()]

    return sum(do_step(grid) for _ in range(100))


def part2(input_txt: str) -> int:
    grid = [[int(x) for x in line] for line in input_txt.splitlines()]

    i = 1
    while True:
        if do_step(grid) == 100:
            return i
        i += 1


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

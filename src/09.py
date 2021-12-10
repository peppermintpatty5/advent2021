#!/usr/bin/env python3

import sys


def is_low(grid: list, r: int, c: int) -> bool:
    rows = len(grid)
    cols = len(grid[0])

    x = grid[r][c]
    return (
        (r == 0 or grid[r - 1][c] > x)
        and (c == 0 or grid[r][c - 1] > x)
        and (r == rows - 1 or grid[r + 1][c] > x)
        and (c == cols - 1 or grid[r][c + 1] > x)
    )


def part1(input_txt: str) -> int:
    grid = [[int(x) for x in line] for line in input_txt.splitlines()]
    rows = len(grid)
    cols = len(grid[0])
    tot = 0

    for r in range(rows):
        for c in range(cols):
            x = grid[r][c]
            if is_low(grid, r, c):
                tot += 1 + x
    return tot


def part2(input_txt: str) -> int:
    grid = [[int(x) for x in line] for line in input_txt.splitlines()]
    rows = len(grid)
    cols = len(grid[0])
    basins = [{(r, c)} for r in range(rows) for c in range(cols) if is_low(grid, r, c)]

    for b in basins:
        while True:
            old_size = len(b)
            adj = set.union(
                *(
                    {
                        (r0, c0)
                        for r0, c0 in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]
                        if 0 <= r0 < rows
                        and 0 <= c0 < cols
                        and grid[r0][c0] > grid[r][c]
                        and grid[r0][c0] != 9
                    }
                    for (r, c) in b
                )
            )
            b |= adj
            if old_size == len(b):
                break
    s = sorted(basins, key=lambda b: len(b), reverse=True)
    return len(s[0]) * len(s[1]) * len(s[2])


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

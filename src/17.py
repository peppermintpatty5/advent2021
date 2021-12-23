#!/usr/bin/env python3

import re
import sys


def part1(input_txt: str) -> int:
    # assume 0 < x1 < x2 and y1 < y2 < 0
    x1, x2, y1, y2 = (int(x) for x in re.findall(r"-?\d+", input_txt))
    return y1 * (y1 + 1) // 2


def part2(input_txt: str) -> int:
    # assume 0 < x1 < x2 and y1 < y2 < 0
    x1, x2, y1, y2 = (int(x) for x in re.findall(r"-?\d+", input_txt))

    count = 0
    for vix in range(1, x2 + 1):
        for viy in range(y1, -y1 + 1):
            x, y = (0, 0)
            vx, vy = (vix, viy)
            while x <= x2 and y1 <= y:
                if x1 <= x <= x2 and y1 <= y <= y2:
                    count += 1
                    break
                x += vx
                y += vy
                vx = max(0, vx - 1)
                vy = vy - 1
    return count


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys


def part1(input_txt: str) -> int:
    lines = []
    for line in input_txt.splitlines():
        p1, p2 = line.split(" -> ")
        p1 = tuple(map(int, p1.split(",")))
        p2 = tuple(map(int, p2.split(",")))
        lines.append((p1, p2))

    point_count = {}
    for ((x1, y1), (x2, y2)) in lines:
        if x1 == x2 or y1 == y2:
            delta = abs(x1 - x2) or abs(y1 - y2)
            x_step = (x2 - x1) / delta
            y_step = (y2 - y1) / delta

            for i in range(delta + 1):
                point = (x1 + i * x_step, y1 + i * y_step)
                point_count[point] = point_count.get(point, 0) + 1

    return sum(1 for v in point_count.values() if v >= 2)


def part2(input_txt: str) -> int:
    lines = []
    for line in input_txt.splitlines():
        p1, p2 = line.split(" -> ")
        p1 = tuple(map(int, p1.split(",")))
        p2 = tuple(map(int, p2.split(",")))
        lines.append((p1, p2))

    point_count = {}
    for ((x1, y1), (x2, y2)) in lines:
        delta = abs(x1 - x2) or abs(y1 - y2)
        x_step = (x2 - x1) / delta
        y_step = (y2 - y1) / delta

        for i in range(delta + 1):
            point = (x1 + i * x_step, y1 + i * y_step)
            point_count[point] = point_count.get(point, 0) + 1

    return sum(1 for v in point_count.values() if v >= 2)


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

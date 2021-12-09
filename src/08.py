#!/usr/bin/env python3

import sys


def part1(input_txt: str) -> int:
    left_sides = []
    right_sides = []
    for line in input_txt.splitlines():
        a, b = line.split(" | ")
        left_sides.append(a.split())
        right_sides.append(b.split())

    return sum(sum(1 for x in item if len(x) in (2, 3, 4, 7)) for item in right_sides)


def calc_output(left_side: list, right_side: list) -> int:
    """
    Calculate the 4-digit output value of the entry.
    """
    unique_patterns = {2: "1", 3: "7", 4: "4", 7: "8"}
    signal_patterns = [set(x) for x in left_side]
    p = {}

    # identify the 1, 4, 7, and 8
    for pattern in signal_patterns:
        if len(pattern) in unique_patterns:
            digit = unique_patterns[len(pattern)]
            p[digit] = pattern

    # identify the 0, 6, and 9
    for pattern in signal_patterns:
        if len(pattern) == 6:
            if p["4"] <= pattern:
                p["9"] = pattern
            elif p["1"] <= pattern:
                p["0"] = pattern
            else:
                p["6"] = pattern

    # identify the 2, 3, and 5
    for pattern in signal_patterns:
        if len(pattern) == 5:
            if p["1"] <= pattern:
                p["3"] = pattern
            elif pattern <= p["6"]:
                p["5"] = pattern
            else:
                p["2"] = pattern

    p_inv = {"".join(sorted(pattern)): digit for digit, pattern in p.items()}

    return int("".join(p_inv["".join(sorted(x))] for x in right_side))


def part2(input_txt: str) -> int:
    left_sides = []
    right_sides = []
    for line in input_txt.splitlines():
        a, b = line.split(" | ")
        left_sides.append(a.split())
        right_sides.append(b.split())

    return sum(calc_output(l, r) for l, r in zip(left_sides, right_sides))


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

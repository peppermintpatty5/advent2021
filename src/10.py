#!/usr/bin/env python3

import sys
from functools import reduce
from typing import Optional


def part1(input_txt: str) -> int:
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0

    for line in input_txt.splitlines():
        stack = []
        for c in line:
            if c in "([{<":
                stack.append(c)
            else:
                p = stack.pop()
                if p + c not in ("()", "[]", "{}", "<>"):
                    total += points[c]
                    break
    return total


def auto_complete(line: str) -> Optional[str]:
    """
    Determines the sequence of characters which if appended to the given line
    would make it complete. `None` is returned for corrupted lines.
    """
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []

    for c in line:
        if c in pairs:
            stack.append(c)
        elif (stack.pop(), c) not in pairs.items():
            return None

    return "".join(pairs[c] for c in reversed(stack))


def part2(input_txt: str) -> int:
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    caps = [auto_complete(line) for line in input_txt.splitlines()]
    scores = [
        reduce(lambda a, b: 5 * a + points[b], x, 0) for x in caps if x is not None
    ]
    scores.sort()
    return scores[len(scores) // 2]


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

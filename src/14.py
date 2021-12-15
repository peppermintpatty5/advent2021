#!/usr/bin/env python3

import sys


def part1(input_txt: str) -> int:
    top_txt, bottom_txt = input_txt.split("\n\n")
    polymer = top_txt
    rules = dict(line.split(" -> ") for line in bottom_txt.splitlines())

    for _ in range(10):
        polymer = (
            "".join(
                polymer[i] + rules.get(polymer[i : i + 2], "")
                for i in range(len(polymer) - 1)
            )
            + polymer[-1]
        )

    char_count = {}
    for c in polymer:
        char_count[c] = char_count.get(c, 0) + 1

    return max(char_count.values()) - min(char_count.values())


def part2(input_txt: str) -> int:
    top_txt, bottom_txt = input_txt.split("\n\n")
    polymer = top_txt
    rules = dict(line.split(" -> ") for line in bottom_txt.splitlines())

    char_count = {}
    for c in polymer:
        char_count[c] = char_count.get(c, 0) + 1

    pair_count = {}
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        pair_count[pair] = pair_count.get(pair, 0) + 1

    for _ in range(40):
        pair_delta = {}
        for (a, b), n in pair_count.items():
            if a + b in rules:
                c = rules[a + b]
                char_count[c] = char_count.get(c, 0) + n
                pair_delta[a + c] = pair_delta.get(a + c, 0) + n
                pair_delta[c + b] = pair_delta.get(c + b, 0) + n
                pair_delta[a + b] = pair_delta.get(a + b, 0) - n
        for k, v in pair_delta.items():
            pair_count[k] = pair_count.get(k, 0) + v

    return max(char_count.values()) - min(char_count.values())


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

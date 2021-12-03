#!/usr/bin/env python3

import sys


def part1(input_txt: str) -> int:
    values = input_txt.splitlines()
    n = len(values)
    k = len(values[0])
    gamma = epsilon = ""

    for i in range(k):
        if 2 * sum(int(v[i]) for v in values) >= n:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, base=2) * int(epsilon, base=2)


def part2(input_txt: str) -> int:
    values = input_txt.splitlines()
    k = len(values[0])
    oxy = list(values)
    co2 = list(values)

    for i in range(k):
        oxy_common = "1" if 2 * sum(int(v[i]) for v in oxy) >= len(oxy) else "0"
        co2_common = "1" if 2 * sum(int(v[i]) for v in co2) >= len(co2) else "0"

        if len(oxy) > 1:
            oxy = [v for v in oxy if v[i] == oxy_common]
        if len(co2) > 1:
            co2 = [v for v in co2 if v[i] != co2_common]

    return int(oxy[0], base=2) * int(co2[0], base=2)


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

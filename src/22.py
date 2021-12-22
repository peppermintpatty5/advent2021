#!/usr/bin/env python3

import re
import sys
from itertools import product


def part1(input_txt: str) -> int:
    cubes = set()
    for line in input_txt.splitlines():
        x1, x2, y1, y2, z1, z2 = (int(x) for x in re.findall(r"-?\d+", line))
        if all(-50 <= t <= 50 for t in (x1, x2, y1, y2, z1, z2)):
            stuff = set(
                product(range(x1, x2 + 1), range(y1, y2 + 1), range(z1, z2 + 1))
            )
            if line.startswith("on"):
                cubes |= stuff
            else:
                cubes -= stuff
    return len(cubes)


def part2(input_txt: str) -> int:
    layers = []
    for line in input_txt.splitlines():
        on = line.startswith("on")
        x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"-?\d+", line))
        layers.append(
            {
                "on": on,
                "x1": x1,
                "x2": x2 + 1,
                "y1": y1,
                "y2": y2 + 1,
                "z1": z1,
                "z2": z2 + 1,
            }
        )
    layers.reverse()

    x_divs = sorted({l["x1"] for l in layers} | {l["x2"] for l in layers})
    y_divs = sorted({l["y1"] for l in layers} | {l["y2"] for l in layers})
    z_divs = sorted({l["z1"] for l in layers} | {l["z2"] for l in layers})

    count = 0
    for i in range(len(x_divs) - 1):
        print(f"iteration {i + 1} / {len(x_divs) - 1}", file=sys.stderr)
        for j in range(len(y_divs) - 1):
            for k in range(len(z_divs) - 1):
                (x, y, z) = (x_divs[i], y_divs[j], z_divs[k])
                (x2, y2, z2) = (x_divs[i + 1], y_divs[j + 1], z_divs[k + 1])
                for l in layers:
                    if (
                        l["x1"] <= x < l["x2"]
                        and l["y1"] <= y < l["y2"]
                        and l["z1"] <= z < l["z2"]
                    ):
                        if l["on"]:
                            count += (x2 - x) * (y2 - y) * (z2 - z)
                        break
    return count


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

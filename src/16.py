#!/usr/bin/env python3

import sys
from math import prod


OP_SUM = 0
OP_PRODUCT = 1
OP_MINIMUM = 2
OP_MAXIMUM = 3
LITERAL_VALUE = 4
OP_GREATER_THAN = 5
OP_LESS_THAN = 6
OP_EQUAL_TO = 7


def parse_packet(bits: str) -> dict:
    """
    Parse string of 1s and 0s into a packet object.
    """
    version = int(bits[0:3], base=2)
    type_id = int(bits[3:6], base=2)
    subpackets = []
    value = None
    i = 6

    if type_id == LITERAL_VALUE:
        value = 0
        while True:
            group = int(bits[i : i + 5], base=2)
            value <<= 4
            value |= group & 0xF
            i += 5
            if not group & 0x10:
                break
    else:
        length_type_id = int(bits[i : i + 1], base=2)
        i += 1
        if length_type_id == 0:
            total_length_of_subpackets = int(bits[i : i + 15], base=2)
            i += 15
            j = 0
            while j < total_length_of_subpackets:
                sub = parse_packet(bits[i:])
                subpackets.append(sub)
                j += sub["length"]
                i += sub["length"]
        else:
            num_subpackets = int(bits[i : i + 11], base=2)
            i += 11
            for _ in range(num_subpackets):
                sub = parse_packet(bits[i:])
                subpackets.append(sub)
                i += sub["length"]

    return {
        "version": version,
        "type_id": type_id,
        "subpackets": subpackets,
        "value": value,
        "length": i,
    }


def version_sum(packet: dict) -> int:
    """
    Recursively calculate the sum of version numbers in packet.
    """
    return packet["version"] + sum(version_sum(sub) for sub in packet["subpackets"])


def part1(input_txt: str) -> int:
    bits = "".join(f"{int(x, base=16):04b}" for x in input_txt.strip())
    return version_sum(parse_packet(bits))


def packet_eval(packet: dict) -> int:
    """
    Evaluate the expression represented by the packet.
    """
    type_id = packet["type_id"]
    subpackets = packet["subpackets"]

    if type_id == OP_SUM:
        return sum(packet_eval(p) for p in subpackets)
    elif type_id == OP_PRODUCT:
        return prod(packet_eval(p) for p in subpackets)
    elif type_id == OP_MINIMUM:
        return min(packet_eval(p) for p in subpackets)
    elif type_id == OP_MAXIMUM:
        return max(packet_eval(p) for p in subpackets)
    elif type_id == LITERAL_VALUE:
        return packet["value"]
    elif type_id == OP_GREATER_THAN:
        return 1 if packet_eval(subpackets[0]) > packet_eval(subpackets[1]) else 0
    elif type_id == OP_LESS_THAN:
        return 1 if packet_eval(subpackets[0]) < packet_eval(subpackets[1]) else 0
    elif type_id == OP_EQUAL_TO:
        return 1 if packet_eval(subpackets[0]) == packet_eval(subpackets[1]) else 0


def part2(input_txt: str) -> int:
    bits = "".join(f"{int(x, base=16):04b}" for x in input_txt.strip())
    return packet_eval(parse_packet(bits))


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

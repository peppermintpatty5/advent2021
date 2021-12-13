#!/usr/bin/env python3

import sys
from typing import Dict, Iterable, List, Tuple


def adjacency_list(edges: Iterable[Tuple[str, str]]) -> Dict[str, List[str]]:
    """
    Convert a sequence of undirected edge pairs into an adjacency "list".
    """
    adj = {}

    for e1, e2 in edges:
        if e1 not in adj:
            adj[e1] = []
        if e2 not in adj:
            adj[e2] = []

        adj[e1].append(e2)
        adj[e2].append(e1)

    return adj


def find_paths1(
    adj: Dict[str, List[str]], prev: List[str] = ["start"]
) -> List[List[str]]:
    """
    Find list of all paths from "start" to "end" that don't contain duplicate
    small nodes.
    """
    paths = []

    for neighbor in adj[prev[-1]]:
        if neighbor.isupper() or neighbor not in prev:
            if neighbor == "end":
                paths += [prev + [neighbor]]
            else:
                paths += find_paths1(adj, prev + [neighbor])

    return paths


def part1(input_txt: str) -> int:
    edges = (tuple(e.split("-")) for e in input_txt.splitlines())

    return len(find_paths1(adjacency_list(edges)))


def find_paths2(
    adj: Dict[str, List[str]], prev: List[str] = ["start"]
) -> List[List[str]]:
    """
    Find list of all paths from "start" to "end" that contain at most one
    duplicate pair of small nodes.
    """
    paths = []
    any_small_duplicates = any(prev.count(s) > 1 for s in prev if s.islower())

    for neighbor in adj[prev[-1]]:
        if (
            neighbor.isupper()
            or neighbor not in prev
            or (neighbor != "start" and not any_small_duplicates)
        ):
            if neighbor == "end":
                paths += [prev + [neighbor]]
            else:
                paths += find_paths2(adj, prev + [neighbor])

    return paths


def part2(input_txt: str) -> int:
    edges = (tuple(e.split("-")) for e in input_txt.splitlines())

    return len(find_paths2(adjacency_list(edges)))


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

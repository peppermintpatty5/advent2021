#!/usr/bin/env python3

import sys


def bingo(board: list, called: set) -> bool:
    """
    Determine if the board has bingo based on the set of called numbers.
    """
    transpose = list(zip(*board))
    return any(all(x in called for x in row) for row in board) or any(
        all(x in called for x in row) for row in transpose
    )


def part1(input_txt: str) -> int:
    lines = input_txt.splitlines()
    pool = list(map(int, lines[0].split(",")))
    boards = [
        [list(map(int, row.split())) for row in b.split("\n")]
        for b in input_txt.split("\n\n")[1:]
    ][:-1]

    called = set()
    for i in range(len(pool)):
        called.add(pool[i])

        for board in boards:
            if bingo(board, called):
                return (
                    sum(sum(x for x in row if x not in called) for row in board)
                    * pool[i]
                )


def part2(input_txt: str) -> int:
    lines = input_txt.splitlines()
    pool = list(map(int, lines[0].split(",")))
    boards = [
        list(list(map(int, row.split())) for row in b.split("\n"))
        for b in input_txt.split("\n\n")[2:]
    ]

    called = set()
    for i in range(len(pool)):
        called.add(pool[i])

        boards = [b for b in boards if not bingo(b, called)]

        if len(boards) == 1:
            board = boards.pop()
            while not bingo(board, called):
                i += 1
                called.add(pool[i])
            return (
                sum(sum(x for x in row if x not in called) for row in board) * pool[i]
            )


def main():
    input_txt = sys.stdin.read()
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()

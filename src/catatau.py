#!/usr/bin/env python3

import sys
from collections.abc import Generator
from functools import singledispatch
from io import TextIOWrapper

STDIN_DEFAULT_NAME = "-"


def file_to_text_wrapper(file_name: str) -> TextIOWrapper:
    return open(file_name, mode="r", encoding="utf-8")


def text_wrapper_iter_lines(
    text_io_wrapper: TextIOWrapper,
) -> Generator[str, None, None]:
    with text_io_wrapper as f:
        yield from map(lambda line: line.rstrip("\n"), f)


@singledispatch
def iter_file(file_name: str) -> Generator[str, None, None]:
    yield from text_wrapper_iter_lines(file_to_text_wrapper(file_name))


@iter_file.register
def _(file_name: TextIOWrapper) -> Generator[str, None, None]:
    yield from text_wrapper_iter_lines(file_name)


def main(file_names: list[str]) -> None:
    new_file_names = map(
        lambda file_name: file_name if file_name != STDIN_DEFAULT_NAME else sys.stdin,
        file_names,
    )
    for file_curr in map(iter_file, new_file_names):
        for line in file_curr:
            print(line)


if __name__ == "__main__":
    main(sys.argv[1:])

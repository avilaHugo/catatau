#!/usr/bin/env python3

import gzip
import sys
from collections.abc import Generator
from typing import Protocol

# Constants
STDIN_DEFAULT_NAME = "-"
DEFAULT_ENCODING = "utf-8"

# Types
StringGenerator = Generator[str, None, None]


class FlatTextFIle:
    def __init__(self, handle: str):
        self.handle = handle

    def iter_file(self) -> StringGenerator:
        with open(self.handle, mode="r", encoding=DEFAULT_ENCODING) as f:
            yield from map(lambda line: line.rstrip("\n"), f)


class GzipTextFIle(FlatTextFIle):
    def iter_file(self) -> StringGenerator:
        with gzip.open(self.handle, mode="rt", encoding=DEFAULT_ENCODING) as f:
            yield from map(lambda line: line.rstrip("\n"), f)


class StdinTextFile(FlatTextFIle):
    _was_readed: bool = False

    def __init__(self, handle: str) -> None:
        if self.__class__._was_readed:
            raise RuntimeError(
                f"Cannot read from stdin more than once: class {self.__class__.__name__} was instanciated more than one time."
            )

        self.__class__._was_readed = True
        super().__init__(handle)

    def iter_file(self) -> StringGenerator:
        with sys.stdin as f:
            yield from map(lambda line: line.rstrip("\n"), f)


class SupportsIterFile(Protocol):
    def iter_file(self) -> StringGenerator:
        ...


def pick_file_parser(handle: str) -> SupportsIterFile:
    def is_gzip(handle: str) -> bool:
        with open(handle, mode="rb") as f:
            return f.read(2) == b"\x1f\x8b"

    def is_stdin(handle: str) -> bool:
        return handle == STDIN_DEFAULT_NAME

    if is_stdin(handle):
        return StdinTextFile(handle)

    if is_gzip(handle):
        return GzipTextFIle(handle)

    return FlatTextFIle(handle)


def main(file_names: list[str]) -> None:
    for file_name in file_names:
        for line in pick_file_parser(file_name).iter_file():
            print(line)


if __name__ == "__main__":
    main(sys.argv[1:])

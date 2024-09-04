#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import functools as ft
import collections.abc as c
from typing import Self
from numbers import Number
import itertools as it

class 

class Stream(c.Iterator):
    def __init__(
        self,
        handle: str,
        separator: str = ";",
        header: c.Iterable[str | int] | None = None
    ) -> None:
        self.data = self._init_stream(handle)
        self.current = next(self.data)
        self.header = header if header else tuple(range(0, len(self.current)))

    def _init_stream(self) -> c.Iterator[Row]:
        with open(self.handle, mode='r') as f:
            yield from map(lambda line: line.rstrip('\n').split(self.separator), f)

    def __iter__(self) -> Self:
        return self
    
    def __next__(self) -> c.Generator[Row, None, None]:
        _next = next(self.data, None)
        if None:
            raise StopIteration
        yield next

def main(file_names: c.Iterable[str]) -> None:
    for file_name in file_names:
        print(Stream(handle=file_name))


if __name__ == "__main__":

    args = argparse.ArgumentParser()
    args.add_argument(
        "file_names",
        nargs="+",
        action="extend",
    )
    main(**vars(args.parse_args()))

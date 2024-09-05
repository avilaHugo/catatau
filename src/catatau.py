#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import collections.abc as c
import typing as t
from functools import reduce


class Series(c.Mapping):
    def __init__(self, data: c.Sequence, name: None) -> None:
        self.data = data
        self.name = name


class DataFrame(c.Mapping):
    def __init__(self, data: dict[str | int, Series]) -> None:
        self.data = data


def iter_file(file_name: str) -> c.Iterator[str]:
    with open(file_name, mode="r") as f:
        yield from map(lambda line: line.rstrip("\n"), f)


def compose(*functions: c.Callable) -> c.Callable:
    return reduce(
        lambda inner, outter: lambda value: outter(inner(value)),
        functions,
        lambda value: value,
    )


# def read_csv(file_name: str, separator=",") -> DataFrame:
#     return DataFrame(dict(zip())


def main(file_names: c.Iterable[str]) -> None:
    for file_name in file_names:
        print(*map(lambda line: line.split(";"), iter_file(file_name)), sep="\n")
        compose(
            iter_file,
        )(file_name)


if __name__ == "__main__":

    args = argparse.ArgumentParser()
    args.add_argument(
        "file_names",
        nargs="+",
        action="extend",
    )
    main(**vars(args.parse_args()))

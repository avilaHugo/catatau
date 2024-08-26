#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import os
import sys
from typing import Iterable, Protocol


class Series(Iterable):
    def __init__(self, data: Iterable, name=str | int | None) -> None:
        self.data = data
        self.name = name


class DataFrame:
    def __init__(self, data: dict[str, Series]) -> None:
        self.data = data

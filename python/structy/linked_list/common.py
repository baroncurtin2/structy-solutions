from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    val: str | int | None
    next: Self = None

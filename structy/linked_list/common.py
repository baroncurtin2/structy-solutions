from dataclasses import dataclass
from typing import Self


@dataclass(slots=True)
class Node:
    val: str | int | None
    next: Self = None

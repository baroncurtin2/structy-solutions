from dataclasses import dataclass
from typing import Optional, Self

NodeValue = Optional[int | str]


@dataclass
class Node:
    val: NodeValue
    left: Optional[Self] = None
    right: Optional[Self] = None

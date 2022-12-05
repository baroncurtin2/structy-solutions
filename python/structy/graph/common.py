from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

NodeValue = Optional[int | str]
Graph = dict[NodeValue, list[NodeValue]]


@dataclass
class Edges:
    edge_list: list[tuple]

    def to_graph(self):
        graph = defaultdict(list)

        for (node_a, node_b) in self.edge_list:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        return graph
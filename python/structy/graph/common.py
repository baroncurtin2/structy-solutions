from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

NodeValue = Optional[int | str]
Graph = dict[NodeValue, list[NodeValue]]
Grid = list[list[str]]
EdgeList = list[tuple | list]


@dataclass
class Edges:
    edge_list: EdgeList

    def to_graph(self):
        graph = defaultdict(list)

        for (node_a, node_b) in self.edge_list:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        return graph


@dataclass
class Prereqs:
    pre_reqs_list: EdgeList

    def to_graph(self):
        graph = defaultdict(list)

        for (a, b) in self.pre_reqs_list:
            graph[a].append(b)

        return graph

from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

NodeValue = Optional[int | str]
Graph = dict[NodeValue, list[NodeValue]]
Grid = list[list[str]]
EdgeList = list[tuple | list]


@dataclass(slots=True)
class Edges:
    edge_list: EdgeList

    def to_graph(self) -> Graph:
        graph = _new_graph()

        for node_a, node_b in self.edge_list:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        return graph

    def to_dag(self) -> Graph:
        graph = _new_graph()

        for start, end in self.edge_list:
            graph[start].append(end)
            _ = graph[end]

        return graph


def _new_graph() -> Graph:
    return defaultdict(list)


@dataclass(slots=True)
class Prereqs:
    pre_reqs_list: EdgeList

    def to_graph(self):
        graph = defaultdict(list)

        for a, b in self.pre_reqs_list:
            graph[a].append(b)

        return graph

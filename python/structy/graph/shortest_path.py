from collections import deque

from structy.graph.common import NodeValue
from .common import Edges


def shortest_path(edges: list[list], node_a: NodeValue, node_b: NodeValue) -> int:
    # e = number edges
    # Time: O(e)
    # Space: O(e)
    if not edges:
        return 0

    if node_a == node_b:
        return 0

    graph = Edges(edges).to_graph()
    visited = set()
    queue = deque([(node_a, 0)])

    while queue:
        current, distance = queue.popleft()

        if current == node_b:
            return distance

        visited.add(current)

        unvisited = [(neighbor, distance + 1) for neighbor in graph[current] if neighbor not in visited]
        queue = deque([*queue, *unvisited])

    return -1

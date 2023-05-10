from collections import deque

from structy.graph.common import NodeValue


def has_path_dfs_recur(graph: dict, src: NodeValue, dst: NodeValue) -> bool:
    if src == dst:
        return True

    return any(has_path_dfs_recur(graph, neighbor, dst) for neighbor in graph[src])


def has_path_dfs_iter(graph: dict, src: NodeValue, dst: NodeValue) -> bool:
    if src == dst:
        return True

    stack = [src]

    while stack:
        current = stack.pop()

        if current == dst:
            return True
        stack = [*stack, *graph[current]]

    return False


def has_path_bfs_iter(graph: dict, src: NodeValue, dst: NodeValue) -> bool:
    if src == dst:
        return True

    queue = deque([src])

    while queue:
        current = queue.popleft()

        if current == dst:
            return True
        queue = deque([*queue, *graph[current]])

    return False

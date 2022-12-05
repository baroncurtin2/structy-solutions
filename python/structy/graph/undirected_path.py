from collections import deque

from structy.graph.common import NodeValue, Edges


def undirected_path_bfs_iter(edge_list: list[tuple], node_a: NodeValue, node_b: NodeValue) -> bool:
    # n = number of nodes
    # e = number edges
    # Time: O(e)
    # Space: O(e)
    if node_a == node_b:
        return True

    edges = Edges(edge_list)
    graph = edges.to_graph()
    visited = set()

    queue = deque([node_a])

    while queue:
        current = queue.popleft()

        if current == node_b:
            return True

        visited.add(current)

        unvisited = [neighbor for neighbor in graph[current] if neighbor not in visited]
        queue = deque([*queue, *unvisited])

    return False


def undirected_path_dfs_iter(edge_list: list[tuple], node_a: NodeValue, node_b: NodeValue) -> bool:
    # n = number of nodes
    # e = number edges
    # Time: O(e)
    # Space: O(e)
    if node_a == node_b:
        return True

    edges = Edges(edge_list)
    graph = edges.to_graph()
    visited = set()

    stack = [node_a]

    while stack:
        current = stack.pop()

        if current == node_b:
            return True

        visited.add(current)

        unvisited = [neighbor for neighbor in graph[current] if neighbor not in visited]
        stack = [*stack, *unvisited]

    return False


def undirected_path_dfs_recur(edge_list: list[tuple], node_a: NodeValue, node_b: NodeValue) -> bool:
    # n = number of nodes
    # e = number edges
    # Time: O(e)
    # Space: O(e)

    edges = Edges(edge_list)
    graph = edges.to_graph()
    return _undirected_path_dfs_recur(graph, node_a, node_b, set())


def _undirected_path_dfs_recur(graph: dict, node_a: NodeValue, node_b: NodeValue, visited: set) -> bool:
    if node_a == node_b:
        return True

    if node_a in visited:
        return False

    visited.add(node_a)

    return any(_undirected_path_dfs_recur(graph, neighbor, node_b, visited) for neighbor in graph[node_a])

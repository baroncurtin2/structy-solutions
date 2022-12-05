from structy.graph.common import Graph, NodeValue
from collections import deque


def connected_components_count_iter_bfs(graph: Graph) -> int:
    # n = number of nodes
    # e = number edges
    # Time: O(e)
    # Space: O(n)
    if len(graph) == 0:
        return 0

    count = 0
    visited = set()

    for node in graph:
        if node in visited:
            continue

        visited.add(node)
        queue = deque(graph[node])

        while queue:
            current = queue.popleft()

            visited.add(current)
            unvisited = [neighbor for neighbor in graph[current] if neighbor not in visited and neighbor not in queue]
            queue = deque([*queue, *unvisited])

        # once finished traversing neighbors, it means the end of a connected component
        count += 1

    return count


def connected_components_count_iter_dfs(graph: Graph) -> int:
    # n = number of nodes
    # e = number edges
    # Time: O(e)
    # Space: O(n)
    if len(graph) == 0:
        return 0

    count = 0
    visited = set()

    for node in graph:
        if node in visited:
            continue

        visited.add(node)
        stack = graph[node]

        while stack:
            current = stack.pop()

            visited.add(current)
            unvisited = [neighbor for neighbor in graph[current] if neighbor not in visited]
            stack = [*stack, *unvisited]

        # once finished traversing neighbors, it means the end of a connected component
        count += 1

    return count


def connected_components_count_recur(graph: Graph) -> int:
    # n = number of nodes
    # e = number edges
    # Time: O(e)
    # Space: O(n)
    visited = set()

    return sum(_dfs(graph, node, visited) for node in graph)


def _dfs(graph: Graph, node: NodeValue, visited: set) -> bool:
    if node in visited:
        return False

    visited.add(node)

    for neighbor in graph[node]:
        _dfs(graph, neighbor, visited)

    return True

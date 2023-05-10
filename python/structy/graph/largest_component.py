from structy.graph.common import Graph, NodeValue

from collections import deque


def largest_component_bfs(graph: Graph) -> int:
    # n = number of nodes
    # e = number edges
    # Time: O(e)
    # Space: O(n)
    if len(graph) == 0:
        return 0

    largest = 0
    visited = set()

    for node in graph:
        if node in visited:
            continue

        current_count = 1
        visited.add(node)
        queue = deque(graph[node])

        while queue:
            current = queue.popleft()
            current_count += 1
            visited.add(current)

            unvisited = [neighbor for neighbor in graph[current] if neighbor not in visited and neighbor not in queue]
            queue = deque([*queue, *unvisited])

        # once finished traversing neighbors, it means the end of a connected component
        if current_count > largest:
            largest = current_count

    return largest


def largest_component_dfs(graph: Graph) -> int:
    # n = number of nodes
    # e = number edges
    # Time: O(e)
    # Space: O(n)
    if len(graph) == 0:
        return 0

    largest = 0
    visited = set()

    for node in graph:
        if node in visited:
            continue

        current_count = 1
        visited.add(node)
        stack = graph[node]

        while stack:
            current = stack.pop()
            current_count += 1
            visited.add(current)

            unvisited = [neighbor for neighbor in graph[current] if neighbor not in visited and neighbor not in stack]
            stack = [*stack, *unvisited]

        # once finished traversing neighbors, it means the end of a connected component
        if current_count > largest:
            largest = current_count

    return largest


def largest_component_recur(graph: Graph) -> int:
    if len(graph) == 0:
        return 0

    visited = set()
    largest = 0

    for node in graph:
        size = _explore_size(graph, node, visited)

        if size > largest:
            largest = size

    return largest


def _explore_size(graph: Graph, node: NodeValue, visited: set) -> int:
    if node in visited:
        return 0

    visited.add(node)

    return 1 + sum(_explore_size(graph, neighbor, visited) for neighbor in graph[node])

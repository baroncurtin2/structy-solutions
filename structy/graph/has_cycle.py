from structy.graph.common import Graph, NodeValue


def has_cycle_dfs_iter(graph: Graph) -> bool:
    visited = set()

    for node in graph:
        if node in visited:
            continue
        stack = [node]
        visiting = set()

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            if current in visiting:
                return True

            visiting.add(current)

            neighbors = graph[current]

            if len(neighbors) == 0:
                visited.union(visiting)
                visiting.clear()

            stack = [*stack, *neighbors]

        visited.union(visited)

    return False


def has_cycle_recur(graph: Graph) -> bool:
    visited = set()

    return any(cycle_detect(graph, node, set(), visited) for node in graph)


def cycle_detect(graph: Graph, node: NodeValue, visiting: set, visited: set) -> bool:
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)
    return False

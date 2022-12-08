from structy.graph.common import Graph


def has_cycle_dfs_iter(graph: Graph) -> bool:
    visited = set()

    for node in graph:
        if node in visited:
            return False

        stack = [node]
        visiting = set()

        while stack:
            current = stack.pop()

            if current in visiting:
                return True

            visiting.add(current)

            stack = [*stack, *graph[current]]

        visited.add(node)

    return False

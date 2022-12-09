from .common import Prereqs, NodeValue, Graph


def prereqs_possible_iter(num_courses: int, prereqs: list[tuple[int, int]]) -> bool:
    graph = Prereqs(prereqs).to_graph()

    visited = set()

    for num in range(num_courses):
        if num in visited:
            continue

        stack = [num]
        visiting = set()

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            if current in visiting:
                return False

            visiting.add(current)

            neighbors = graph[current]

            if len(neighbors) == 0:
                visited.union(visiting)
                visiting.clear()

            stack = [*stack, *neighbors]

        visited.union(visited)

    return True


def prereqs_possible_recur(num_courses: int, prereqs: list[tuple[int, int]]) -> bool:
    graph = Prereqs(prereqs).to_graph()

    visited = set()
    visiting = set()

    return not any(has_cycle(graph, node, visiting, visited) for node in range(num_courses))


def has_cycle(graph: Graph, node: NodeValue, visiting: set, visited: set) -> bool:
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if has_cycle(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)

    return False

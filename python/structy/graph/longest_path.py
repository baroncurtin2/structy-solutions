from collections import defaultdict

from structy.graph.common import Graph, NodeValue


def longest_path_dfs(graph: Graph) -> int:
    distance = defaultdict(int, {node: 0 for node in graph if len(graph[node]) == 0})

    for node in graph:
        if node in distance:
            continue

        current_distance = 1
        stack = graph[node]

        while stack:
            current = stack.pop()

            if distance.get(current) == 0:
                continue
            current_distance += 1

            stack = [*stack, *graph[current]]

        distance[node] = max(distance[node], current_distance)

    return max(distance.values())


def longest_path_recur(graph: Graph) -> int:
    distance = defaultdict(int, {node: 0 for node in graph if len(graph[node]) == 0})

    for node in graph:
        _traverse(graph, node, distance)

    return max(distance.values())


def _traverse(graph: Graph, node: NodeValue, distance: defaultdict) -> int:
    if node in distance:
        return distance[node]

    largest = 0
    for neighbor in graph[node]:
        attempt = _traverse(graph, neighbor, distance)

        if attempt > largest:
            largest = attempt

    distance[node] = 1 + largest
    return distance[node]

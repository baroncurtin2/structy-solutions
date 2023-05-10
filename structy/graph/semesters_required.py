from collections import defaultdict

from structy.graph.common import EdgeList, Graph


def semesters_required_dfs(num_courses: int, prereqs: EdgeList) -> int:
    graph = build_graph(prereqs)
    distance = defaultdict(int, {node: 1 for node in graph if len(graph[node]) == 0})

    for num in range(num_courses):
        if (num in distance) and (distance[num] == 1):
            continue

        stack = [(num, 1)]

        while stack:
            current, dis = stack.pop()

            if (current in distance) and (distance[current] == 1):
                distance[num] = max(distance[num], dis)
                continue

            distance[current] = max(distance[current], dis)
            neighbors = [(neighbor, dis + 1) for neighbor in graph[current]]
            stack = [*stack, *neighbors]

    return max(distance.values())


def semesters_required_recur(num_courses: int, prereqs: EdgeList) -> int:
    graph = build_graph(prereqs)
    distance = defaultdict(int, {node: 1 for node in graph if len(graph[node]) == 0})

    for num in range(num_courses):
        _traverse(graph, num, distance)

    return max(distance.values())


def _traverse(graph: Graph, node: int, distance: defaultdict) -> int:
    if node in distance:
        return distance[node]

    max_dis = 0

    for neighbor in graph[node]:
        neighbor_distance = _traverse(graph, neighbor, distance)

        if neighbor_distance > max_dis:
            max_dis = neighbor_distance

    distance[node] = 1 + max_dis
    return distance[node]


def build_graph(pre_reqs: EdgeList) -> Graph:
    graph = defaultdict(list)

    for pre_req in pre_reqs:
        a, b = pre_req
        graph[a].append(b)

    return graph

from collections import defaultdict

from structy.graph.common import EdgeList, Graph


def semesters_required_dfs(num_courses: int, prereqs: EdgeList) -> int:
    graph = build_graph(prereqs)
    distance = defaultdict(int, {node: 0 for node in graph if len(graph[node]) == 0})
    print(distance)

    for node in graph:
        if (node in distance) and (distance[node] == 0):
            continue

        stack = [(node, 1)]

        while stack:
            current, dis = stack.pop()

            if (current in distance) and (distance[current] == 0):
                distance[node] = max(distance[node], dis)
                continue

            distance[current] = max(distance[current], dis)
            neighbors = [(neighbor, dis + 1) for neighbor in graph[current]]
            stack = [*stack, *neighbors]

    return max(distance.values())


def build_graph(pre_reqs: EdgeList) -> Graph:
    graph = defaultdict(list)

    for pre_req in pre_reqs:
        a, b = pre_req
        graph[a].append(b)

    return graph

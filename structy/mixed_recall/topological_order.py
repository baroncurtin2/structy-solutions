from collections import defaultdict


def topological_order(graph: dict[str, list[str]]) -> list[str]:
    num_parents = get_num_parents(graph)

    ready = [node for node in num_parents if num_parents[node] == 0]
    order = []

    while ready:
        node = ready.pop()
        order.append(node)

        for child in graph[node]:
            num_parents[child] -= 1

            if num_parents[child] == 0:
                ready.append(child)

    return order


def get_num_parents(graph: dict[str, list[str]]) -> defaultdict[str, int]:
    num_parents = defaultdict(int)

    for parent in graph:
        for child in graph[parent]:
            num_parents[child] += 1
            _ = num_parents[parent]  # ensures that parent has a key in num_parents

    return num_parents

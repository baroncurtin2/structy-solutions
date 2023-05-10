from structy.mixed_recall.common import UndirectedGraph


def can_color(graph: UndirectedGraph, recur: bool) -> bool:
    return can_color_recur(graph) if recur else can_color_iter(graph)


def can_color_recur(graph: UndirectedGraph) -> bool:
    coloring = {}

    return not any(node not in coloring and not validate(graph, node, coloring, False) for node in graph)


def can_color_iter(graph: dict[str, list[str]]) -> bool:
    coloring: dict[str, bool] = {}

    for node in graph:
        if node in coloring:
            continue

        stack = [(node, False)]

        while stack:
            current_node, current_color = stack.pop()

            if current_node not in coloring:
                coloring[current_node] = current_color

            for neighbor in graph[current_node]:
                if neighbor in coloring:
                    if current_color == coloring[neighbor]:
                        return False
                else:
                    stack = [*stack, (neighbor, not current_color)]
    return True


def validate(graph: UndirectedGraph, node: str, coloring: dict[str, bool], current_color: bool) -> bool:
    if node in coloring:
        return current_color == coloring[node]

    coloring[node] = current_color

    return all(validate(graph, neighbor, coloring, not current_color) for neighbor in graph[node])

from structy.graph.common import EdgeList, Edges, Graph, NodeValue


def rare_routing(n: int, roads: EdgeList, recur: bool = False) -> bool:
    graph = Edges(roads).to_graph()

    return rare_routing_recur(n, graph) if recur else rare_routing_iter(n, graph)


def rare_routing_recur(n: int, graph: Graph) -> bool:
    visited = set()

    valid = validate(graph, 0, visited, None)

    return valid and len(visited) == n


def validate(graph: Graph, node: NodeValue, visited: set, last_node: NodeValue) -> bool:
    if node in visited:
        return False

    visited.add(node)

    return not any(neighbor != last_node and not validate(graph, neighbor, visited, node) for neighbor in graph[node])


def rare_routing_iter(n: int, graph: Graph) -> bool:
    visited = set()
    stack = [(0, None)]

    while stack:
        node, last_node = stack.pop()

        if node in visited:
            return False

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor != last_node:
                stack.append((neighbor, node))

    return len(visited) == n

from structy.graph.common import Edges, Graph
from structy.mixed_recall.common import NodeValue

RivalryList = list[list | tuple]


def tolerant_teams(rivalries: RivalryList, *, recur: bool = False) -> bool:
    graph = Edges(rivalries).to_graph()

    return tolerant_teams_recur(graph) if recur else tolerant_teams_iter(graph)


def tolerant_teams_iter(graph: Graph) -> bool:
    teams = {}

    for node in graph:
        if node in teams:
            continue

        stack = [(node, False)]

        while stack:
            current_node, current_team = stack.pop()

            if current_node not in teams:
                teams[current_node] = current_team

            for neighbor in graph[current_node]:
                if neighbor in teams:
                    if current_team == teams[neighbor]:
                        return False
                else:
                    stack = [*stack, (neighbor, not current_team)]
    return True


def tolerant_teams_recur(graph: Graph) -> bool:
    # e = number of rivalries
    # n = number of people
    # Time: O(e)
    # Space: O(n)
    teams = {}

    return not any(node not in teams and not is_bipartite(graph, node, teams, False) for node in graph)


def is_bipartite(graph: Graph, node: NodeValue, teams: dict[str, bool], current_team) -> bool:
    if node in teams:
        return teams[node] == current_team

    teams[node] = current_team

    return all(is_bipartite(graph, neighbor, teams, not current_team) for neighbor in graph[node])

from structy.graph.common import Edges
from structy.mixed_recall.topological_order import topological_order


def safe_cracking(hints):
    edges = Edges(hints)
    graph = edges.to_dag()

    order = topological_order(graph)
    return "".join([str(num) for num in order])

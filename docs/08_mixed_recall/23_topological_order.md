# topological order

## Description

Write a function, topological_order, that takes in a dictionary representing the adjacency list for a directed-acyclic graph. The function should return a list containing the topological-order of the graph.

The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence.

## Test Cases

test_00:

```text
topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
}) # -> ['c', 'a', 'f', 'b', 'd', 'e']
```

test_01:

```text
topological_order({
  "h": ["l", "m"],
  "i": ["k"],
  "j": ["k", "i"],
  "k": ["h", "m"],
  "l": ["m"],
  "m": [],
}) # -> ['j', 'i', 'k', 'h', 'l', 'm']
```

test_02:

```text
topological_order({
  "q": [],
  "r": ["q"],
  "s": ["r"],
  "t": ["s"],
}) # -> ['t', 's', 'r', 'q']
```

test_03:

```text
topological_order({
  "v": ["z", "w"],
  "w": [],
  "x": ["w", "v", "z"],
  "y": ["x"],
  "z": ["w"],
}) # -> ['y', 'x', 'v', 'z', 'w']
```

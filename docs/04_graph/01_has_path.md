# has path

## Description

Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

Hey. This is our first graph problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

## Test Cases

test_00:

```text
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'k') # True
```

test_01:

```text
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'j') # False
```

test_02:

```text
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'i', 'h') # True
```

test_03:

```text
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],
}

has_path(graph, 'v', 'w') # True
```

test_04:

```text
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],
}

has_path(graph, 'v', 'z') # False
```

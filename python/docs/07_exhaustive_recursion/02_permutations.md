# permutations

## Description

Write a function, permutations, that takes in a list an argument. The function should return a 2D list where each sublist represents one of the possible permutations of the list.

The sublists may be returned in any order.

You may assume that the input list contains unique items.

## Test Cases

test_00:

```text
permutations(['a', 'b', 'c']) # ->
# [
#   [ 'a', 'b', 'c' ],
#   [ 'b', 'a', 'c' ],
#   [ 'b', 'c', 'a' ],
#   [ 'a', 'c', 'b' ],
#   [ 'c', 'a', 'b' ],
#   [ 'c', 'b', 'a' ]
# ]
```

test_01:

```text
permutations(['red', 'blue']) # ->
# [
#   [ 'red', 'blue' ],
#   [ 'blue', 'red' ]
# ]
```

test_02:

```text
permutations([8, 2, 1, 4]) # ->
# [
#   [ 8, 2, 1, 4 ], [ 2, 8, 1, 4 ],
#   [ 2, 1, 8, 4 ], [ 2, 1, 4, 8 ],
#   [ 8, 1, 2, 4 ], [ 1, 8, 2, 4 ],
#   [ 1, 2, 8, 4 ], [ 1, 2, 4, 8 ],
#   [ 8, 1, 4, 2 ], [ 1, 8, 4, 2 ],
#   [ 1, 4, 8, 2 ], [ 1, 4, 2, 8 ],
#   [ 8, 2, 4, 1 ], [ 2, 8, 4, 1 ],
#   [ 2, 4, 8, 1 ], [ 2, 4, 1, 8 ],
#   [ 8, 4, 2, 1 ], [ 4, 8, 2, 1 ],
#   [ 4, 2, 8, 1 ], [ 4, 2, 1, 8 ],
#   [ 8, 4, 1, 2 ], [ 4, 8, 1, 2 ],
#   [ 4, 1, 8, 2 ], [ 4, 1, 2, 8 ]
# ]
```

test_03:

```text
permutations([]) # ->
# [
#  [ ]
# ]
```

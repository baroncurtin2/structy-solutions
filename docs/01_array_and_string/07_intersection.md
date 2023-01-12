# intersection

## Description

Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.

## Test Cases

test_00:

```text
intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
```

test_01:

```text
intersection([2,4,6], [4,2]) # -> [2,4]
```

test_02:

```text
intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
```

test_03:

```text
intersection([0,1,2], [10,11]) # -> []
```

test_04:

```text
a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
intersection(a, b) # -> [0,1,2,3,..., 49999]
```

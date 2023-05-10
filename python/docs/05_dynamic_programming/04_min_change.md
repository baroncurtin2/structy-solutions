# min change

## Description

Write a function min_change that takes in an amount and a list of coins. The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary.

If it is not possible to create the amount, then return -1.

## Test Cases

test_00:

```text
min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
```

test_01:

```text
min_change(13, [1, 9, 5, 14, 30]) # -> 5
```

test_02:

```text
min_change(23, [2, 5, 7]) # -> 4
```

test_03:

```text
min_change(102, [1, 5, 10, 25]) # -> 6
```

test_04:

```text
min_change(200, [1, 5, 10, 25]) # -> 8
```

test_05:

```text
min_change(2017, [4, 2, 10]) # -> -1
```

test_06:

```text
min_change(271, [10, 8, 265, 24]) # -> -1
```

test_07:

```text
min_change(0, [4, 2, 10]) # -> 0
```

test_08:

```text
min_change(0, []) # -> 0
```

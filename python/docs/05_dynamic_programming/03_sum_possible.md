# sum possible

## Description

Write a function sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.

## Test Cases

test_00:

```text
sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
```

test_01:

```text
sum_possible(15, [6, 2, 10, 19]) # -> False
```

test_02:

```text
sum_possible(13, [6, 2, 1]) # -> True
```

test_03:

```text
sum_possible(103, [6, 20, 1]) # -> True
```

test_04:

```text
sum_possible(12, []) # -> False
```

test_05:

```text
sum_possible(12, [12]) # -> True
```

test_06:

```text
sum_possible(0, []) # -> True
```

test_07:

```text
sum_possible(271, [10, 8, 265, 24]) # -> False
```

test_08:

```text
sum_possible(2017, [4, 2, 10]) # -> False
```

test_09:

```text
sum_possible(13, [3, 5]) # -> true
```

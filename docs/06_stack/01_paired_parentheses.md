# paired parentheses

## Description

Write a function, paired_parentheses, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'.

## Test Cases

test_00:

```text
paired_parentheses("(david)((abby))") # -> True
```

test_01:

```text
paired_parentheses("()rose(jeff") # -> False
```

test_02:

```text
paired_parentheses(")(") # -> False
```

test_03:

```text
paired_parentheses("()") # -> True
```

test_04:

```text
paired_parentheses("(((potato())))") # -> True
```

test_05:

```text
paired_parentheses("(())(water)()") # -> True
```

test_06:

```text
paired_parentheses("(())(water()()") # -> False
```

test_07:

```text
paired_parentheses("") # -> True
```

test_08:

```text
pairedParentheses("))()") # False
```

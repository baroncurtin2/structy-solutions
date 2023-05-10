# befitting brackets

## Description

Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }

## Test Cases

test_00:

```text
befitting_brackets('(){}[](())') # -> True
```

test_01:

```text
befitting_brackets('({[]})') # -> True
```

test_02:

```text
befitting_brackets('[][}') # -> False
```

test_03:

```text
befitting_brackets('{[]}({}') # -> False
```

test_04:

```text
befitting_brackets('[]{}(}[]') # -> False
```

test_05:

```text
befitting_brackets('[]{}()[]') # -> True
```

test_06:

```text
befitting_brackets(']{}') # -> False
```

test_07:

```text
befitting_brackets('') # -> True
```

test_08:

```text
befitting_brackets("{[(}])") # -> False
```

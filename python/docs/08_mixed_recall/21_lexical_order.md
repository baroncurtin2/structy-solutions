# lexical order

## Description

Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument. The function should return True if the first word should appear before the second word if lexically-ordered according to the given alphabet order. If the second word should appear first, then return False.

Note that the alphabet string may be any arbitrary string.

Intuitively, Lexical Order is like "dictionary" order:

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.

## Test Cases

test_00:

```text
alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("apple", "dock", alphabet) # -> True
```

test_01:

```text
alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("apple", "ample", alphabet) # -> False
```

test_02:

```text
alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("app", "application", alphabet) # -> True
```

test_03:

```text
alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("backs", "backdoor", alphabet) # -> False
```

test_04:

```text
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("zoo", "dinner", alphabet) # -> True
```

test_05:

```text
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("leaper", "leap", alphabet) # -> False
```

test_06:

```text
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("backs", "backdoor", alphabet) # -> True
```

test_07:

```text
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("semper", "semper", alphabet) # -> True
```

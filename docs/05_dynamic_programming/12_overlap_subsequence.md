# overlap subsequence

## Description

Write a function, overlap_subsequence, that takes in two strings as arguments. The function should return the length of the longest overlapping subsequence.

A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.

## Test Cases

test_00:

```text
overlap_subsequence("dogs", "daogt") # -> 3
```

test_01:

```text
overlap_subsequence("xcyats", "criaotsi") # -> 4
```

test_02:

```text
overlap_subsequence("xfeqortsver", "feeeuavoeqr") # -> 5
```

test_03:

```text
overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave") # -> 11
```

test_04:

```text
overlap_subsequence(
  "mumblecorebeardleggingsauthenticunicorn",
  "succulentspughumblemeditationlocavore"
) # -> 15
```

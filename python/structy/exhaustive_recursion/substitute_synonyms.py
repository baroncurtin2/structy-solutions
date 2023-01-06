from dataclasses import dataclass, field


@dataclass(slots=True)
class TrieNode:
    children: dict[str, "TrieNode"] = field(default_factory=dict)
    synonyms: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Trie:
    root: TrieNode = field(default_factory=TrieNode)

    def insert(self, word: str, synonym: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.synonyms.append(synonym)

    def search(self, word: str) -> list[str]:
        node = self.root

        for char in word:
            if char not in node.children:
                return []

            node = node.children[char]
        return node.synonyms


def substitute_synonyms(sentence: str, synonyms: dict[str, list[str]]) -> list[str]:
    # n = number of words in sentence
    # m = max number of synonyms for a word
    # Time: ~O(m^n)
    # Space: ~O(m^n)
    words = sentence.split(" ")

    trie = Trie()

    for word, synonym_list in synonyms.items():
        for synonym in synonym_list:
            trie.insert(word, synonym)

    print(trie)
    substitutions = _substitute_synonyms(words, synonyms, trie, {})
    return [" ".join(sub) for sub in substitutions]


def _substitute_synonyms(words: list[str], synonyms: dict[str, list[str]], trie: Trie, memo: dict) -> list[list[str]]:
    key = tuple(words)

    if not words:
        return [[]]

    if key in memo:
        return memo[key]

    first = words[0]
    remaining = words[1:]
    sub_arrays = _substitute_synonyms(remaining, synonyms, trie, memo)

    result = []
    if synonym_list := trie.search(first):
        for synonym in synonym_list:
            result.extend([synonym, *sub_array] for sub_array in sub_arrays)
    else:
        result.extend([first, *sub_array] for sub_array in sub_arrays)

    memo[key] = result
    return result

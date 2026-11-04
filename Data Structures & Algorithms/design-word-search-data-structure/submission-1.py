class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            i = ord(c) - ord("a")

            if cur.children[i] is None:
                cur.children[i] = TrieNode()

            cur = cur.children[i]

        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, node):
            if j == len(word):
                return node.endOfWord

            c = word[j]

            if c == ".":
                for child in node.children:
                    if child is not None and dfs(j + 1, child):
                        return True
                return False

            i = ord(c) - ord("a")

            if node.children[i] is None:
                return False

            return dfs(j + 1, node.children[i])

        return dfs(0, self.root)
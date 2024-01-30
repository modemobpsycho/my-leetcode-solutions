class TrieNode:
    def __init__(self) -> None:
        self.children: dict = {}
        self.end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr: TrieNode = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr: TrieNode = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr: TrieNode = self.root
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i - 1]
        return True

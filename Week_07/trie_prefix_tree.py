#208. 实现 Trie (前缀树)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node[self.end] = self.end

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w  in word:
            if w not in node:
                return False
            node = node[w]
        if self.end in node:
            return True
        return False

            



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w not in node:
                return False
            node = node[w]
        return True
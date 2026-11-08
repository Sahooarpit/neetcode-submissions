class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        node = self.root
        for c in word:
            pos = ord(c) - ord('a')

            if not node.children[pos]:
                node.children[pos] = TrieNode()
            
            node = node.children[pos]
        node.endOfWord = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                return False
            node = node.children[pos]
        
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for c in prefix:
            pos = ord(c) - ord('a')
            if not node.children[pos]:
                return False
            node = node.children[pos]

        
        return True
        
        
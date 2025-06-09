class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # check if char in word is in children, if not, add it to map which points to a node
        # update counter, and set last character word to true
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() # create a new node with empty children
            curr = curr.children[c] # point to child node
        curr.word = True 

    def search(self, word: str) -> bool:
        # iterate through trie and return word
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
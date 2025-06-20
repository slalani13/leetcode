# create a prefix and suffix tree (this goes through each letter and adds it to the tree)
# n words * m letters

# words = ["dog", "cat", "dig"]
# prefix = d, suffix = g
# return 2
# tree -> d -> o -> g, True, 0
#           -> i -> g, True, 2
# tree -> g -> o -> d, True, 0
#.          -> i -> d, True, 2

# return all words with prefix -> dog, dig O(m*n)
# return all words with suffix -> dog, dig
# match words in both sets, return highest index O(n)

class TrieNode:

    def __init__(self):
        self.children = {} # char : trienode
        self.isWord = False
        self.index = None
    
    # adds word to prefix Tree
    def addWord(self, word, idx) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True
        curr.index = idx

    # returns set of word indices with prefix
    def search(self, prefix):
        res = set()
        curr = self
        for char in prefix:
            if char not in curr.children:
                return res
            curr = curr.children[char]
        self.dfs(curr, res)
        return res
    
    # helper to fill out set of word indices with prefix
    def dfs(self, node, res) -> None: # O(m words * n length)
        if not node:
            return res
        if node.isWord:
            res.add(node.index)
        for child in node.children.values():
            self.dfs(child, res)

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.prefixTree = TrieNode()
        self.suffixTree = TrieNode()
        for index, word in enumerate(words):
            self.prefixTree.addWord(word, index)
            reversedWord = word[::-1]
            self.suffixTree.addWord(reversedWord, index)


    def f(self, pref: str, suff: str) -> int:
        prefixIndexes = self.prefixTree.search(pref)
        suffixIndexes = self.suffixTree.search(suff[::-1])
        matches = prefixIndexes.intersection(suffixIndexes)
        return max(matches) if len(matches) > 0 else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
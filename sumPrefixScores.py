class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += 1

    def find_score(self, word):
        curr = self.root
        score = 0

        for c in word:
            curr = curr.children[c]
            score += curr.count
        return score    

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        res = []
        for word in words:
            res.append(trie.find_score(word))
        return res

        
        

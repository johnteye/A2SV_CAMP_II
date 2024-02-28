class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True
    
    def search(self, word:str) -> bool:
        curr = self.root
        prefix = ""
        for c in word:
            idx = ord(c) - ord("a")
            if not curr.children[idx]:
                return prefix
            prefix += c    
            curr = curr.children[idx]    
        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()
        tree = Trie()
        tree.insert(strs[0])

        res = ""
        for i in strs[1:]:
            res = tree.search(i)

        return res if len(strs) >= 2 else strs[0]

    
        

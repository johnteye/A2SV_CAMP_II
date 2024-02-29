class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True


    def search(self, word: str) -> bool:
        curr = self.root
        
        def helper(curr, idx):
            res = False
            
            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children:
                        res = res or helper(curr.children[child], i+1)
                    return res

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.is_end

        return helper(curr, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

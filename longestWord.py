class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True





class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # words.sort()
        trie = Trie()
        root = trie.root
        for word in words:
            trie.insert(word)
        longest_word = ""
        

        queue = deque([])
        for value, child in root.children.items():
            if child.is_end:
                queue.append(( value,child))

        while queue:
            level_count = len(queue)
            for i in range(level_count):
                curr_value, curr_child = queue.popleft()
                for value, child in curr_child.children.items():
                    if child.is_end:   
                        queue.append((curr_value + value, child))

                if len(curr_value) > len(longest_word) or (len(curr_value) == len(longest_word) and curr_value < longest_word):
                    longest_word = curr_value



        return longest_word


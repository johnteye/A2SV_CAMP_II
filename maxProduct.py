class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def word_to_mask(word):
            mask =  0
            for c in word:
                mask |= 1 << ord(c) - ord("a")
                
            return mask
        max_product =  0

        masks = [word_to_mask(word) for word in words]

        for i in range(len(words)):
            for j in range(i +  1, len(words)):
                if masks[i] & masks[j] ==  0:
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)

        return max_product

        

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        res, total =  0, 0
        
        for val in satisfaction:
            total += val
            if total <=  0:
                break
            res += total
        return res
               
                    

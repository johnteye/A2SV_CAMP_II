class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        check = sum(nums) / 2
        
        def dp(i, j, turn):
            if i > j:
                return 0

            if turn:
                return max(nums[i]+ dp(i+1, j, False), nums[j]+ dp(i, j-1, False))

            else:
                return min(dp(i+1, j, True) , dp(i, j-1,True))

    
        return dp(0, len(nums)-1, True) >= check 

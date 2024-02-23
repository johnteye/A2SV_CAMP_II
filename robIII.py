# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(node):
            if not node:
                return [0, 0]

            if node in memo:
                return memo[node]

            left =  dp(node.left)
            right = dp(node.right)

            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)

            memo[node] = [rob, not_rob]

            return memo[node]

        return max(dp(root))

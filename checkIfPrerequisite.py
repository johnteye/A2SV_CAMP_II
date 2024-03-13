class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    
        dp = [[False]* (numCourses) for _ in range(numCourses)]

        for src, des in prerequisites:
            dp[src][des] = True

        for i in range(numCourses):
            dp[i][i] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])
        
        # print(dp)
        res = []
        for src, des in queries:
            res.append(dp[src][des])
        return res
        
        

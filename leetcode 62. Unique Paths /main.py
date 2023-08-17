class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # at least 1 path existed in the grid
        dp =  [[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                # b/c all possible path to the current dp[i][j] is sum(dp previous; i-direction and j-direction)
                dp[i][j]= dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
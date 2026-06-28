class Solution:
    def climbStairs(self, n: int) -> int:
        # top-down DP
        # arr =[-1 for _ in range(n)]
        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     if arr[i] != -1:
        #         return arr[i]
        #     arr[i] = dfs(i+1) + dfs(i+2)
        #     return arr[i]
        # return dfs(0)

        if n <= 2:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount +1 for _ in range(amount+1)]
        dp[0] = 0

        for e in range(1, amount+1):
            for c in coins:
                if e-c >= 0:
                    dp[e] = min(dp[e], 1 + dp[e-c])
                    
        return dp[amount] if dp[amount] != amount+1 else -1
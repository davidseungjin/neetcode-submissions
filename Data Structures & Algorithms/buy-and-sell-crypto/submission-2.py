class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        # res = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         res = max(res, prices[j]-prices[i])
        # return res

        # Other than brute force, I had no idea
        l = 0
        r = 1
        res = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                lval = prices[r] - prices[l]
                res = max(res, lval)
            else:
                l = r
            r += 1
        return res

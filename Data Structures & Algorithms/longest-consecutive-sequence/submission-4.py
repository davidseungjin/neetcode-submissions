class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        res = 0
        for n in hset:
            if (n-1) not in hset:
                lval = 1
                while (n+lval) in hset:
                    lval += 1
                res = max(res, lval)
        return res
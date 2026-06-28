class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # xorr = n
        # for i in range(n):
        #     xorr = xorr^(i^nums[i])
        # return xorr
        # ==================
        # Bit-wise solution
        # ==================   

        # n = len(nums)
        # out = 0
        # for x in range(1,n+1):
        #     out = out ^ x
        # for y in nums:
        #     out = out ^ y

        # return out


        # =============
        # Easy solution
        # =============

        n = len(nums)
        target = n * (n + 1) // 2
        return target - sum(nums)
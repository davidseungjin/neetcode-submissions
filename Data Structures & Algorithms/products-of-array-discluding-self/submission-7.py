class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
        # prefix = [1 for _ in nums]
        # suffix = [1 for _ in nums]
        # for i in range(1, len(nums)):
        #     prefix[i] = prefix[i-1] * nums[i-1]
        # for i in range(len(nums)-2, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i+1]
        # res = [0 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     res[i] = (prefix[i]* suffix[i])
        # return res
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        # two max values
        arr = [0 for i in range(len(nums))]
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            arr[i] = max(arr[i-1], arr[i-2]+nums[i])
        
        return arr[-1]
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        
        # arr = [False for _ in range(len(nums))]
        # arr[-1] = True

        # for i in range(len(nums)-1, -1, -1):
        #     if i + nums[i] > len(nums)-1:
        #         continue
        #     if arr[i+nums[i]]:
        #         arr[i] = True
        # return arr[0]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
        # l = 0
        # r = len(nums) - 1
        # res = nums[0]

        # while l <= r:
        #     if nums[l] <= nums[r]:
        #         res = min(res, nums[l])
        #         break
        #     else:
        #         mid = (l + r) // 2
        #         res = min(res, nums[mid])
        #         if nums[l] <= nums[mid]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        # return res
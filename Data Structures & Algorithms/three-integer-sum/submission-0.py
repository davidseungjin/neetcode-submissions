class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # diff
        
        
        # prepare the result array
        res = []
        # sort
        nums.sort()

        for i, a in enumerate(nums):
            # if the lowest value is greater than zero, end
            if a > 0:
                break

            # if the value is same as previous
            # skip because these cases are handled already 
            # with while loop
            if i > 0 and a == nums[i - 1]:
                continue

            # consider a as a constant,
            # so l starts from i+1
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # additional step to prevent duplicate
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
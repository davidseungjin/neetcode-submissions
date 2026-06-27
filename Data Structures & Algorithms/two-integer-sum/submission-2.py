class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for i, e in enumerate(nums):
            t = target - e
            if t in hmap:
                return [hmap[t], i]
            hmap[e] = i
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for e in nums:
            if e in hset:
                return True
            hset.add(e)
        return False
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        # since it is not sorted, it should be sorted first
        # to maintain the original index, make it tuple first before sort

        tuple_arr = [(e, i) for i, e in enumerate(nums)]
        tuple_arr.sort(key=lambda x: x[0])
        while i < j:
            t = tuple_arr[i][0] + tuple_arr[j][0]
            if t == target:
                return sorted([tuple_arr[i][1], tuple_arr[j][1]])
            elif t > target:
                j -= 1
            else:
                i += 1 
        return []
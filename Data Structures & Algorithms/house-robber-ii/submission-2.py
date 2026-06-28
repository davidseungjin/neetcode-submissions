class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        
        n = len(nums)
        arr1 = nums[:n-1]
        arr2 = nums[1:]

        def getmax(arr):
            temparr = [0 for _ in range(len(arr))]
            temparr[0] = arr[0]
            temparr[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                temparr[i] = max(temparr[i-1], temparr[i-2]+arr[i])
            return temparr[-1]
        res1 = getmax(arr1)
        res2 = getmax(arr2)
        return max(res1, res2)
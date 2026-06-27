class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # area = distance x min(height)

        # 1. brute force
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         val = (j - i) * min(heights[i], heights[j])
        #         res = max(res, val)
        # return res

        # another
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            localarea = (r-l) * min(heights[l], heights[r])
            res = max(res, localarea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
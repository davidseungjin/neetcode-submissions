class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # area = distance x min(height)

        # 1. brute force
        res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                val = (j - i) * min(heights[i], heights[j])
                res = max(res, val)
        return res
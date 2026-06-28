class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = 0
        # for i in range(32):
        #     if (1 << i) & n:
        #        res += 1
        # return res 

        val = n
        res = 0
        while val:
            if val & 1:
                res += 1
            val >>= 1
        return res
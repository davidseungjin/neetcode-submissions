class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #study two things
        # brute force and sliding window

        hset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            res = max(res, r - l + 1)
        return res

        # optimal 
        # mp = {}
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     if s[r] in mp:
        #         l = max(mp[s[r]] + 1, l)
        #     mp[s[r]] = r
        #     res = max(res, r - l + 1)
        # return res
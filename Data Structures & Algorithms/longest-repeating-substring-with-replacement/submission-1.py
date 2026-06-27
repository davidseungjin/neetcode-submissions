class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # give up
        hmap = defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            hmap[s[r]] += 1
            maxf = max(maxf, hmap[s[r]])

            while (r-l+1) - maxf > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        return res
        # count = {}
        # res = 0

        # l = 0
        # maxf = 0
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     maxf = max(maxf, count[s[r]])

        #     while (r - l + 1) - maxf > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(res, r - l + 1)

        # return res
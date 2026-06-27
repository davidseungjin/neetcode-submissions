class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = defaultdict(int)
        for e in nums:
            fmap[e] += 1
        arr = [(k, v) for k, v in fmap.items()]
        arr.sort(key=lambda x: x[1], reverse=True)

        res = arr[:k]
        return [e[0] for e in res]
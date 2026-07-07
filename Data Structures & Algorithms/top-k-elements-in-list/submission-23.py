class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = dict()
        for e in nums:
            hmap[e] = hmap.get(e, 0) + 1

        heap = []
        for e in hmap.keys():
            heapq.heappush(heap, (hmap[e], e))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
        # hmap = defaultdict(int)
        # for e in nums:
        #     hmap[e] += 1
        
        # arr = []
        # for key, val in hmap.items():
        #     arr.append((val, key))
        # arr.sort()
        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res
        
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # for num, cnt in count.items():
        #     freq[cnt].append(num)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
                    
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res


        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res
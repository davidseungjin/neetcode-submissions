class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            hmap[key].append(s)
        
        return [v for k, v in hmap.items()]
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ss = dict()
        tt = dict()
        for i in range(len(s)):
            ss[s[i]] = 1 + ss.get(s[i], 0)
            tt[t[i]] = 1 + tt.get(t[i], 0)
        
        for e in ss:
            if ss[e] != tt.get(e, 0):
                return False
        return True

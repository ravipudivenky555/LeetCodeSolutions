class Solution:
    def firstUniqChar(self, s: str) -> int:
        res=dict()
        for c in s:
            res[c]=res.get(c,0)+1
        for k,v in res.items():
            if v==1:
                return s.index(k)
        return -1
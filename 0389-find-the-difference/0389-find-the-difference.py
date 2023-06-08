from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1=Counter(s)
        c2=Counter(t)
        s=set(t)-set(s)
        if len(s)>0:
            for i in s:
                return i
        for i in c1:
            if c1[i]!=c2[i]:
                return i
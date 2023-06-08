class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        t1,t2=dict(),dict()
        for c in s:
            t1[c]=t1.get(c,0)+1
        for c in t:
            t2[c]=t2.get(c,0)+1
        for i in t1:
            if t2.get(i,0)!=0 and t1[i]==t2[i]:
                del t2[i]
        if len(t2.items())>0:
            return False
        return True
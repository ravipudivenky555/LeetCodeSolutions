class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        u=len(s)
        l=0
        perm=[]
        for i in range(u):
            if s[i]=='I':
                perm.append(l)
                l+=1
            else:
                perm.append(u)
                u-=1
        perm.append(l)
        return perm
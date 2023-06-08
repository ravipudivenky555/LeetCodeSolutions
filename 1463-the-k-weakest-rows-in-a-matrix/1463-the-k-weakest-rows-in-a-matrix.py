class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowStrength=[]
        for i in mat:
            total=0
            for j in i:
                if j==1:
                    total+=1
                else:
                    break
            rowStrength.append(total)
        weakRows=[]
        for i in rowStrength:
            if len(weakRows)==k:
                strongest=max(weakRows)
                if strongest<i:
                    continue
                weakRows.remove(strongest)
            weakRows.append(i)
        weakRows=sorted(weakRows)
        n=len(weakRows)
        for i in range(n):
            ind=rowStrength.index(weakRows[i])
            rowStrength[ind]=-1
            weakRows[i]=ind
        return weakRows
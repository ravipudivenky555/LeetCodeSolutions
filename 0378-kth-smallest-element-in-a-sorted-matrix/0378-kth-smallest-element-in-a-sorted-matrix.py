class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        eles=[]
        for i in matrix:
            eles.extend(i)
        eles.sort()
        return eles[k-1]
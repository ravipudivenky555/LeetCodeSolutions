from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        fin = 0
        for i in range(len(points)-1):
            first = points[i]
            second = points[i+1]
            res = [e2 - e1 for e2,e1 in zip(second,first)]
            fin += abs(max(res, key=abs))
        return(fin)
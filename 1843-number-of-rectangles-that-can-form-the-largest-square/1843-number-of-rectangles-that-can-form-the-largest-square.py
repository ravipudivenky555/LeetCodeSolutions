class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen=0
        c=0
        for i in rectangles:
            currLen=min(i)
            if currLen>maxLen:
                maxLen=currLen
                c=1
            elif currLen==maxLen:
                c+=1
        return c
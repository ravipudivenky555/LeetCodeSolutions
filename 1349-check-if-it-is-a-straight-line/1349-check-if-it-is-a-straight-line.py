class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        try:
            x,y=coordinates[0]
            x1,y1=coordinates[1]
            m=(y-y1)/(x-x1)
            x,y=x1,y1
            for i,j in coordinates:
                m1=(y-j)/(x-i)
                x,y=i,j
                if m!=m1:return False
        except ZeroDivisionError:
            for i in coordinates:
                if x!=i[0]:
                    return False
        return True
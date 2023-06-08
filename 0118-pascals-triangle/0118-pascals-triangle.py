class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1],[1,1]]
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return res
        for i in range(numRows-2):
            newRow=[1]
            for i in range(len(res[-1])-1):
                newRow.append(res[-1][i]+res[-1][i+1])
            newRow.append(1)
            res.append(newRow)
        return res
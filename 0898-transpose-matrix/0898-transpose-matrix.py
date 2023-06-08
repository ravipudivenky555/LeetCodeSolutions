class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        i=0
        while i<len(matrix[0]):
            row=[]
            j=0
            while j<len(matrix):
                row.append(matrix[j][i])
                j+=1
            res.append(row)
            i+=1
        return res
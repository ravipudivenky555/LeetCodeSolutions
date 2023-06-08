class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        row=[1]
        ind=0
        while ind<rowIndex:
            ind+=1
            r=[1]
            ele=row.pop(0)
            while row:
                ele1=row.pop(0)
                r.append(ele+ele1)
                ele=ele1
            r.append(1)
            row=r
            print(row)
        return row
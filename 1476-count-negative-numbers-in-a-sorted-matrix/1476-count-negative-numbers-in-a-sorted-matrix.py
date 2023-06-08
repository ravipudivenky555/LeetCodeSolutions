class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i,j,c=0,len(grid[0]),0
        while i<len(grid) and j>0:
            if grid[i][j-1]<0:
                j-=1
            else:
                c+=len(grid[i][j:])
                i+=1
        c+=(len(grid)-i)*len(grid[0])
        return c
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        while k>0:
            t=grid[m-1][n-1]
            i=m-1
            while i>=0:
                j=n-1
                if i<m-1:
                    grid[i+1][0]=grid[i][j]
                while j>0:
                    grid[i][j]=grid[i][j-1]
                    j-=1
                i-=1
            grid[0][0]=t
            k-=1
        return grid
from queue import PriorityQueue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ans = 0
        q = PriorityQueue()
        q.put((0,0,0))
        Y = len(heights) - 1
        X = len(heights[0]) - 1
        while True :
            dif, y, x = q.get()
            if heights[y][x] == 0 : continue
            ans = max(ans, dif)
            if y == Y and x == X : break 
            if y != 0 and heights[y-1][x] != 0 :
                q.put( (abs(heights[y][x] - heights[y-1][x]), y-1, x) )
            if y != Y and heights[y+1][x] != 0 :
                q.put( (abs(heights[y][x] - heights[y+1][x]), y+1, x) )
            if x != 0 and heights[y][x-1] != 0 :
                q.put( (abs(heights[y][x] - heights[y][x-1]), y, x-1) )
            if x != X and heights[y][x+1] != 0 :
                q.put( (abs(heights[y][x] - heights[y][x+1]), y, x+1) )
            heights[y][x] = 0
        return ans
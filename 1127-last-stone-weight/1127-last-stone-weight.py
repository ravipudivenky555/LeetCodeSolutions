class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        while n>1:
            stones.sort()
            if stones[n-1]==stones[n-2]:
                stones.pop()
                stones.pop()
            elif stones[n-1]>stones[n-2]:
                y=stones.pop()
                x=stones.pop()
                stones.append(y-x)
            n=len(stones)
        if n==0:
            return 0
        elif n==1:
            return stones.pop()
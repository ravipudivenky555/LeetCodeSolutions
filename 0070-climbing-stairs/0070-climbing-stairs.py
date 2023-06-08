class Solution:
    def climbStairs(self, n: int) -> int:
        l=[1,1]+[-1]*(n-1)
        def fun(n):
            if l[n]==-1:
                l[n]=fun(n-1)+fun(n-2)
            return l[n]
        return fun(n)
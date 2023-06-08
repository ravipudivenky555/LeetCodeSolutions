class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        resList=[0]*(n+1)
        resList[1]=1
        def fibHelper(n):
            if n>2:
                fibHelper(n-1)
            resList[n]=resList[n-1]+resList[n-2]
        fibHelper(n)
        return resList[-1]
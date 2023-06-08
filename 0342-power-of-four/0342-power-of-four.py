class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        while n&3==0:
            n=n>>2
        return n==1
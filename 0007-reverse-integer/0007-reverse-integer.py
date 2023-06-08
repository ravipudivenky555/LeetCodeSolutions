class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        sign=0
        if x<0:
            sign=1
            x=0-x
        while x>0:
            rev=rev*10+x%10
            x=x//10
        if sign:
            rev=0-rev
        if rev<(-(2**(31))) or rev>((2**31)-1):
            return 0
        return rev
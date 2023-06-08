# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        h=n
        while l<=h:
            m=(l+h)//2
            if isBadVersion(m):
                if isBadVersion(m-1)==False:
                    return m
                h=m-1
            else:
                if isBadVersion(m+1):
                    return m+1
                l=m+1
        return m
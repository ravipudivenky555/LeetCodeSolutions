class Solution:
    def countSegments(self, s: str) -> int:
        res=s.split()
        if res==['']:return 0
        return len(res)
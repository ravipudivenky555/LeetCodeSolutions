class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s1=[]
        while s:
            s1.append(s.pop())
        while s1:
            s.append(s1.pop(0))
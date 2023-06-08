class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        if len(needle)==len(haystack):
            return 0 if needle==haystack else -1
        i,j=0,len(needle)
        while i+j<=len(haystack):
            if haystack[i:i+j]==needle:
                return i
            i+=1
        return -1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in strs:
            for j in range(min(len(prefix),len(i))):
                if prefix[j]==i[j]:
                    continue
                else:
                    prefix=prefix[:j]
                    break
            if prefix.startswith(i):
                prefix=i
        return prefix
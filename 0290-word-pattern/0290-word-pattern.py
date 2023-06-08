class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        if len(set(pattern))!=len(set(words)):
            return False
        patternBuffer=dict()
        for i in range(len(pattern)):
            if words[i] not in patternBuffer:
                patternBuffer[words[i]]=pattern[i]
            elif patternBuffer[words[i]]!=pattern[i]:
                return False
        return True
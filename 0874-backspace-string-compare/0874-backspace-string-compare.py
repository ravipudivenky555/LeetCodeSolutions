class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack=list()
        tstack=list()
        for char in s:
            if char=='#':
                try:
                    sstack.pop()
                finally:
                    continue
            sstack.append(char)
        for char in t:
            if char=='#':
                try:
                    tstack.pop()
                finally:
                    continue
            tstack.append(char)
        i=0
        while i<min(len(tstack),len(sstack)):
            if tstack[i]!=sstack[i]:
                return False
            i+=1
        if i<len(sstack) or i<len(tstack):
            return False
        return True
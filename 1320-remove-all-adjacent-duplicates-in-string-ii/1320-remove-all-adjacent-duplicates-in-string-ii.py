class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[['X',0]]
        for i in s:
            if stack[-1][0]==i:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([i,1])
        return ''.join(c*n for c,n in stack)
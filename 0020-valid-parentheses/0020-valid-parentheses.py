class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:return False
                t=stack.pop()
                if i==')' and t!='(':
                    return False
                if i==']' and t!='[':
                    return False
                if i=='}' and t!='{':
                    return False
        return not stack
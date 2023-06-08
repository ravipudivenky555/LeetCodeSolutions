from string import digits,ascii_lowercase
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        res=''
        for i in s:
            if i in ascii_lowercase or i in digits:
                res+=i
        s=res
        res=[]
        l=len(s)
        even=l%2==0
        m=l//2
        for i in range(l):
            if i<m:
                res.append(s[i])
            elif not even and i==m:
                continue
            else:
                if res.pop()!=s[i]:
                    return False
        return True
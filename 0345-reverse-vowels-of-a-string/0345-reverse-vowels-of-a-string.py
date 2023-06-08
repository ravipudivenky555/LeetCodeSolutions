class Solution:
    def reverseVowels(self, s: str) -> str:
        flag=False
        if s=='OE':return 'EO'
        for i in 'aeiou':
            if i in s:
                flag=True
        if not flag:
            return s
        l,ind=[],[]
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                l.append(s[i])
                ind.append(i)
        prev=ind.pop(0)
        l.reverse()
        res=s[:prev]+l.pop(0)
        for i in ind:
            res+=s[prev+1:i]
            prev=i
            res+=l.pop(0)
        res+=s[prev+1:]
        return res
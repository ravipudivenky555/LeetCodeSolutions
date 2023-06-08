class Solution:
    def romanToInt(self, s: str) -> int:
        value=0
        romanValue={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        n=len(s)
        continueFlag=0
        for i in range(n):
            if continueFlag>0:
                continueFlag-=1
                continue
            if i<n-1:
                if romanValue[s[i]]<romanValue[s[i+1]]:
                    value+=(romanValue[s[i+1]]-romanValue[s[i]])
                    continueFlag=1
                else:
                    value+=romanValue[s[i]]
            else:
                value+=romanValue[s[i]]
        return value
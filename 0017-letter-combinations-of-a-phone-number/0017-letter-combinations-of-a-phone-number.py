class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        for digit in digits:
            if digit=="2":
                letters=['a','b','c']
            elif digit=="3":
                letters=['d','e','f']
            elif digit=="4":
                letters=['g','h','i']
            elif digit=="5":
                letters=['j','k','l']
            elif digit=="6":
                letters=['m','n','o']
            elif digit=="7":
                letters=['p','q','r','s']
            elif digit=="8":
                letters=['t','u','v']
            elif digit=="9":
                letters=['w','x','y','z']
            if not res:
                res.extend(letters)
                continue
            j=0
            result=[]
            while j<len(res):
                for k in letters:
                    result.append(res[j]+k)
                j+=1
            res=result
        return res
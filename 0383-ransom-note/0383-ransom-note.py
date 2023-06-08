class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n=len(ransomNote)
        for i in range(n):
            if ransomNote[i] in magazine:
                magazine=magazine.replace(ransomNote[i]," ",1)
            else:
                return False
        return True
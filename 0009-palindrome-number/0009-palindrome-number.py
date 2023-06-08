class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        temp=x
        sign=0
        if x<0:
            return False
        while temp:
            rev=rev*10+temp%10
            temp=temp//10
        return rev==x
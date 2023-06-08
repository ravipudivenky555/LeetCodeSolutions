class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            dup=0
            while num>0:
                dup+=num%10
                num=num//10
            num=dup
        return num
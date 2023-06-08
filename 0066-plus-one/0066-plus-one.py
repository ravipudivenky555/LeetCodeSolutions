class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        i=len(digits)-1
        while i>=0:
            digits[i]=digits[i]+carry
            carry=0
            if digits[i]==10 and i>0:
                digits[i]=0
                carry=1
            elif digits[i]==10 and i==0:
                digits[i]=0
                digits.insert(0,1)
            i-=1
        return digits
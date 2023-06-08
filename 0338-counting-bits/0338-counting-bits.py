class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        def bin(n):
            if n==0:return ''
            if n%2==0:return bin(n//2)+'0'
            else:return bin(n//2)+'1'
        for i in range(n+1):
            res.append(bin(i).count('1'))
        return res
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquare(n)
            if n == 1:
                return True
        return False
    def sumOfSquare(self,n) -> int:
        output = 0
        while n > 0:
            digits = n % 10
            digits = digits * digits
            output += digits
            n = n // 10
        return output
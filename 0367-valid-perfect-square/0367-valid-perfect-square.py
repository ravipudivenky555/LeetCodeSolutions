import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(math.sqrt(num))**2==num
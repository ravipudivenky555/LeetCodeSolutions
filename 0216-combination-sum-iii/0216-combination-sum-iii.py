class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, n, low):
            if k == 1:
                return [[n]] if low <= n <= 9 else []
            res = []
            for num in range(low, 10):
                for combo in helper(k - 1, n - num, num + 1):
                    combo.append(num)
                    res.append(combo)
            return res
        return helper(k, n, 1)
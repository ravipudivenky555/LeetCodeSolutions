class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = collections.defaultdict(lambda: 0)
        res = 0
        for num in nums:
            if counter[k - num]:
                counter[k - num] -= 1
                res += 1
            else:
                counter[num] += 1
        return res
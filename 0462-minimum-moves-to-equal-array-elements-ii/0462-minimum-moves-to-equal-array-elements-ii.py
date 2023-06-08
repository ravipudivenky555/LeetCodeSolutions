class Solution:
    def minMoves2(self, nums):
        nums = sorted(nums)
        median = nums[len(nums)//2]
        res = 0
        for n in nums:
            res += abs(n-median)
        return res
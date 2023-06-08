class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k<=len(nums):
            nums.sort()
            return nums[-k]
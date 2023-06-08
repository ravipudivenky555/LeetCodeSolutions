class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start = -1
        end = -2
        for i, num in enumerate(sorted(nums)):
            if num != nums[i]:
                if start == -1:
                    start = i
                else:
                    end = i
        return end - start + 1
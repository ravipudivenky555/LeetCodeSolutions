class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        n=len(nums)
        nums.sort()
        if n > 2:
            return nums[n-3]
        else:
            return nums[n-1]
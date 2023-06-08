class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums):
            if nums[i]==i:
                i+=1
                continue
            return i
        return i
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                nums.pop(i)
                continue
            i+=1
        return len(nums)
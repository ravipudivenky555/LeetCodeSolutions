class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target>nums[-1]:
            return len(nums)
        elif target<nums[0]:
            return 0
        l,h=0,len(nums)-1
        m=0
        while l<=h:
            m=(l+h)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            elif nums[m]>target:
                h=m-1
        return l
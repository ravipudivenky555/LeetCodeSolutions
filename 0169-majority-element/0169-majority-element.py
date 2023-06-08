class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=0
        c=0
        for i in set(nums):
            if nums.count(i)>c:
                ele=i
                c=nums.count(i)
        return ele
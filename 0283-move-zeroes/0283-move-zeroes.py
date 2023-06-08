class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=nums.count(0)
        i=0
        while c>0:
            if nums[i]==0:
                nums.append(nums.pop(i))
                c-=1
            else:i+=1
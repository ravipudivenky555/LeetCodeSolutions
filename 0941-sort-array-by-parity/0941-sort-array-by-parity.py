class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            even=0
            odd=0
            for j in range(len(nums)):
                if nums[j]%2:
                    odd=j
                    break
            for j in range(odd,len(nums)):
                if not nums[j]%2:
                    even=j
                    break
            if even>0:
                temp=nums[odd]
                nums[odd]=nums[even]
                nums[even]=temp
        return nums
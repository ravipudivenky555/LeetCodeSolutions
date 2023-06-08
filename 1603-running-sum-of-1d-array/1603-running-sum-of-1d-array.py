class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        runningSum=0
        while i<len(nums):
            runningSum+=nums[i]
            res.append(runningSum)
            i+=1
        return res
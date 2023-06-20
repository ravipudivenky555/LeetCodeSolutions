class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k==0:return nums.copy()
        res=[-1]*len(nums)
        d=2*k+1
        sumEle=0
        try:
            for i in range(2*k):sumEle+=nums[i]
            for i in range(k,len(nums)-k):
                sumEle+=nums[i+k]
                res[i]=sumEle//d
                sumEle-=nums[i-k]
            return res
        except:return res
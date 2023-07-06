class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen=float('inf')
        total=nums[0]
        start=0
        end=1
        while end<=len(nums):
            try:
                if total>=target:
                    minLen=min(minLen,end-start)
                    total-=nums[start]
                    start+=1
                else:
                    if end==len(nums):
                        if minLen==float('inf'):
                            return 0
                        else:
                            return minLen
                    total+=nums[end]
                    end+=1
            except:break
        if end==len(nums) and minLen==float('inf'):
                return 0
        return minLen
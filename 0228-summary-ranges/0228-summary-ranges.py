class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        begin=str(nums[0])
        ans=list()
        end=str(nums[0])
        for i in range(len(nums)):
            if i==len(nums)-1:
                if begin!=end:
                    ans.append(begin+"->"+end)
                else:
                    ans.append(begin)
            else:
                if nums[i]+1==nums[i+1] or nums[i]==nums[i+1]:
                    end=str(nums[i+1])
                else:
                    if begin!=end:
                        ans.append(begin+"->"+end)
                    else:
                        ans.append(begin)
                    begin=str(nums[i+1])
                    end=str(nums[i+1])
        return ans
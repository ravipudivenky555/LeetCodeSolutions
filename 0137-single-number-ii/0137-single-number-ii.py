class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=dict()
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if d[i]==1:
                return i
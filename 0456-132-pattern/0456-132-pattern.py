class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        i=len(nums)-1
        stack=[]
        j=-math.inf
        while i>=0:
            if nums[i]<j:
                return True
            while stack and stack[-1]<nums[i]:
                j=stack.pop()
            stack.append(nums[i])
            i-=1
        return False
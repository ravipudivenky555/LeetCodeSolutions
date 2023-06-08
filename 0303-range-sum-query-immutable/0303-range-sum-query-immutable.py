class NumArray:
    def __init__(self, nums: List[int]):
        self.pf = nums[::]
        for x in range(1,len(self.pf)): self.pf[x] += self.pf[x-1]
    def sumRange(self, left: int, right: int) -> int:
        return self.pf[right] if left == 0 else self.pf[right]-self.pf[left-1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
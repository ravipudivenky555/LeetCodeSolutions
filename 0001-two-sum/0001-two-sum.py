class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for index, val in enumerate(nums):
            comp[val] = index
        for index, val in enumerate(nums):
            num_to_find = target - val
            if num_to_find in comp and comp[num_to_find] != index:
                return [index, comp[num_to_find]]
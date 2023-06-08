class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        counter = Counter(nums)
        def findAllPermutations(res):
            if len(res) == len(nums):
                permutations.append(res)
                return
            for key in counter:
                if counter[key]:
                    counter[key]-=1
                    findAllPermutations(res + [key])
                    counter[key]+=1
        findAllPermutations([])
        return permutations
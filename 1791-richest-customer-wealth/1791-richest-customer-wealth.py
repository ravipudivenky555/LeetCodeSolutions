def wealth(accounts:List[int])->int:
    sumofwealth=0
    for i in accounts:
        sumofwealth+=i
    return sumofwealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth=0
        for i in accounts:
            maxWealth=max(maxWealth,wealth(i))
        return maxWealth
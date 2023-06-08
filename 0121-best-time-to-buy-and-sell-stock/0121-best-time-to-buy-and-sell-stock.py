class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        price=float('inf')
        for i in prices:
            if i<price:
                price=i
            profit=max(profit,i-price)
        return profit
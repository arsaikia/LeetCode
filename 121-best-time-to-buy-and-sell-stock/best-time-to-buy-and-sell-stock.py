class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice, maxProfit = float("inf"), 0

        for price in prices:
            buyPrice = min(buyPrice, price)
            profit = price - buyPrice
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
        
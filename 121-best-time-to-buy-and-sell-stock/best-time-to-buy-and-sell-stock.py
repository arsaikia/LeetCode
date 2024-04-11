class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        buyPrice = float("inf")

        for r in range(len(prices)):
            currPrice = prices[r]

            # update buy price, if curr price is less that previous buy price
            buyPrice = min(buyPrice, currPrice)

            profit = currPrice - buyPrice

            maxProfit = max(maxProfit, profit)
        
        return maxProfit


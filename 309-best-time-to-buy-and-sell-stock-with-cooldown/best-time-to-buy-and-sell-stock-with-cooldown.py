class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}
        def backtrack(idx, canBuy):
            if idx >= len(prices):
                return 0

            if (idx, canBuy) in dp:
                return dp[(idx, canBuy)]

            hold = backtrack(idx + 1, canBuy)

            # can buy
            if canBuy:
                buy = backtrack(idx + 1, not canBuy) - prices[idx]
                dp[(idx, canBuy)] = max(buy, hold)

            # can't buy
            else:
                sell = backtrack(idx + 2, not canBuy) + prices[idx]
                dp[(idx, canBuy)] = max(sell, hold)
            
            return dp[(idx, canBuy)]
        
        return backtrack(0, True)

        
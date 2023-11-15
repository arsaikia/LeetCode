class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (idx, isBuying)

        def getProfit(idx, isBuying):

            if idx >= len(prices):
                return 0
            
            if (idx, isBuying) in dp:
                return dp[(idx, isBuying)]
            
            if isBuying:
                buy = getProfit(idx + 1, not isBuying) - prices[idx]
                cooldown = getProfit(idx + 1, isBuying)
                dp[(idx, isBuying)] = max(buy, cooldown)
            else:
                sell = getProfit(idx + 2, not isBuying) + prices[idx]
                cooldown = getProfit(idx + 1, isBuying)
                dp[(idx, isBuying)] = max(sell, cooldown)
            
            return dp[(idx, isBuying)]

        return getProfit(0, True)
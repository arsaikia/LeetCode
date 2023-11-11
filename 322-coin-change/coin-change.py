class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numCoins = [float("inf") for i in range(amount + 1)]
        numCoins[0] = 0

        for denom in coins:
            for am in range(len(numCoins)):
                if denom <= am:
                    numCoins[am] = min(numCoins[am], numCoins[am - denom] + 1)
        
        return numCoins[amount] if numCoins[amount] != float("inf") else -1
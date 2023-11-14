class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0 for i in range(amount + 1)]
        ways[0] = 1

        for denom in coins:
            for value in range(1, amount + 1):
                if denom <= value:
                    ways[value] += ways[value - denom]
        
        return ways[amount]

        
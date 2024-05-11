class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        @cache
        def backtrack(idx, total):

            if total == amount:
                return 1
            
            if idx >= len(coins) or total > amount:
                return 0
            
            ways = 0

            # take current coin -> use same coin again
            ways += backtrack(idx, total + coins[idx])

            # skip curr coin
            ways += backtrack(idx + 1, total)

            return ways
        
        return backtrack(0, 0)
        
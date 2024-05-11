class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def backtrack(idx, need):

            if need == 0:
                return 1
            
            if idx >= len(coins) or need < 0:
                return 0
            
            if (idx, need) in dp:
                return dp[(idx, need)]
            
            ways = 0

            # take current coin -> use same coin again
            ways += backtrack(idx, need - coins[idx])

            # skip curr coin
            ways += backtrack(idx + 1, need)

            dp[(idx, need)] = ways
            return ways
        
        return backtrack(0, amount)
        
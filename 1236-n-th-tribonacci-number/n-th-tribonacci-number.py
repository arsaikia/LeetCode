class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {
            0: 0,
            1: 1,
            2: 1
        }

        def find(n):
            if n == 0:
                return 0
            
            if n in memo:
                return memo[n]

            memo[n] = find(n - 1) + find(n - 2) + find(n - 3)
            return memo[n]
        
        return find(n)
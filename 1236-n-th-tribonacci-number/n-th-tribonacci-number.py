class Solution:
    def tribonacci(self, n: int) -> int:

        @cache
        def find(n):
            if n == 0:
                return 0
            
            if n <= 2:
                return 1

            return find(n - 1) + find(n - 2) + find(n - 3)
        
        return find(n)
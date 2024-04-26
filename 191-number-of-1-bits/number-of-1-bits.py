class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n:
            if n % 2:
                bits += 1
            n = n >> 1
        
        return bits
        
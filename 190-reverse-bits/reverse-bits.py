class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bitFromLST = (n >> i) & 1

            # move the bit to MST
            res = res | (bitFromLST << (31 - i))
        
        return res
        
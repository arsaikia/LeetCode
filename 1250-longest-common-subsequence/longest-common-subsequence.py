class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        cache = [ [0 for col in range(COLS + 1)] for row in range(ROWS + 1) ]

        for row in reversed(range(ROWS)):
            for col in reversed(range(COLS)):
                charOne, charTwo = text1[row], text2[col]
                if charOne == charTwo:
                    cache[row][col] = 1 + cache[row + 1][col + 1]
                else:
                    cache[row][col] = max(cache[row + 1][col], cache[row][col + 1])
        
        return cache[0][0]



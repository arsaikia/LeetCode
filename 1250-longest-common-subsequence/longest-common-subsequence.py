class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def find(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                return 1 + find(i + 1, j + 1)
            
            return max(find(i + 1, j), find(i, j + 1))
        
        return find(0, 0)
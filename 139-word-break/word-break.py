class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:

        dp = {len(s): True}
        def backtrack(i):
            if i in dp:
                return dp[i]
            
            canReach = False
            for word in words:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    if backtrack(i + len(word)):
                        canReach = True
            
            dp[i] = canReach
            return dp[i]
        
        backtrack(0)
        return dp[0]

            
        
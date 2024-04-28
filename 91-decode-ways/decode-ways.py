class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        
        def backtrack(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0
            
            res = backtrack(i + 1)

            # take two
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                res += backtrack(i + 2)
            
            dp[i] = res
            return dp[i]        
        return backtrack(0)
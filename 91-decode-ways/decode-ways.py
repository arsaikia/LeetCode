class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)

        def backtrack(i):
            
            if i == len(s):
                return 1
            
            if dp[i]:
                return dp[i]
            
            ways = 0
            for j in range(i, len(s)):
                if j - i + 1 > 2:
                    continue
                
                ch = s[i : j + 1]

                if ch[0] != "0" and 1 <= int(ch) <= 26:
                    ways += backtrack(j + 1)
            
            dp[i] = ways
            return dp[i]
        
        backtrack(0)
        return dp[0]
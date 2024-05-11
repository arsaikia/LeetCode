class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [ [False for col in range(len(s2) + 1)] for row in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i in reversed(range(len(dp))):
            for j in reversed(range(len(dp[0]))):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        
        return dp[0][0]


        
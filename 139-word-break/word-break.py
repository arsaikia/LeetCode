class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]

        for idx in reversed(range(len(s))):
            for word in wordDict:
                if idx + len(word) <= len(dp) and s[idx : idx + len(word)] == word:
                    if dp[idx]:
                        continue
                    dp[idx] = dp[idx + len(word)]

        return dp[0]

        
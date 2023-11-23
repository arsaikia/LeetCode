class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        visited = collections.defaultdict(int)
        l = 0
        longest = 0
        maxF = 0

        for r in range(len(s)):
            visited[s[r]] += 1
            maxF = max(maxF, visited[s[r]])

            if (r - l + 1) - maxF > k:
                visited[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
        
        return longest
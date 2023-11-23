class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        visited = collections.defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)):
            visited[s[r]] += 1

            while (r - l + 1) - max(visited.values()) > k:
                visited[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
        
        return longest
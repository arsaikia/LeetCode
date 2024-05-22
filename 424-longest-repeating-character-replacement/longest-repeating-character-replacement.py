class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = collections.defaultdict(int)
        maxFreq = 0
        longest = 0
        l = 0

        for r in range(len(s)):
            chars[s[r]] += 1
            maxFreq = max(chars.values())

            if (r - l + 1) - maxFreq > k:
                chars[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))
        
        return longest
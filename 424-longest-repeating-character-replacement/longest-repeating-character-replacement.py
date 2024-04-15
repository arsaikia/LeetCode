class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowChars = collections.defaultdict(int)
        l, res = 0, 0

        for r in range(len(s)):

            windowChars[s[r]] += 1

            # close window if > k after replacing chars
            while (r - l + 1) - max(windowChars.values()) > k:
                windowChars[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

        
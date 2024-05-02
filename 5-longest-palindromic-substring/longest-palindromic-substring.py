class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = [-1, -1]

        for i in range(len(s)):

            # odd pali
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest:
                    longest = r - l + 1
                    res = [l, r]
                l -= 1
                r += 1


            # even pali
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest:
                    longest = r - l + 1
                    res = [l, r]
                l -= 1
                r += 1
        
        l, r = res
        return s[l : r + 1] if longest else ""

        
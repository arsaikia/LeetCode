class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0

        for i in range(len(s)):
            # odd pali
            l, r = i, i
            while l >= 0 and r< len(s) and s[l] == s[r]:
                substrings += 1
                l -= 1
                r += 1
            
            # even pali
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                substrings += 1
                l -= 1
                r += 1
        
        return substrings
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1Chars = [0] * 26
        for char in s1:
            s1Chars[ord(char) - ord("a")] += 1
        
        s2Chars = [0] * 26
        l = 0

        for r in range(len(s2)):
            s2Chars[ord(s2[r]) - ord("a")] += 1

            # close window if in window chars > len(s1)
            while (r - l + 1) > len(s1):
                s2Chars[ord(s2[l]) - ord("a")] -= 1
                l += 1
            
            if (r - l + 1) == len(s1) and s1Chars == s2Chars:
                return True
        
        return False
        
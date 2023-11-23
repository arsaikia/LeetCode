class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Chars = [0] * 26
        s1Set = set(s1)
        for ch in s1:
            s1Chars[ord(ch) - ord("a")] += 1
        
        l = 0
        s2Chars = [0] * 26
        for r in range(len(s2)):
            if s2[r] not in s1Set:
                continue
            
            s2Chars[ord(s2[r]) - ord("a")] += 1

            while r - l + 1 > len(s1):
                if s2[l] in s1Set:
                    s2Chars[ord(s2[l]) - ord("a")] -= 1
                l += 1
            
            if r - l + 1 == len(s1) and s1Chars == s2Chars:
                return True
        
        return False


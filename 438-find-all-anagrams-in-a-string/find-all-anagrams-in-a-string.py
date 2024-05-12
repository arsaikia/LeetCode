class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pChars, sChars = [0] * 26, [0] * 26

        for c in p:
            pChars[ord(c) - ord("a")] += 1
        
        l = 0
        res = []
        for r in range(len(s)):

            sChars[ord(s[r]) - ord("a")] += 1

            if sChars == pChars:
                res.append(l)

            if r - l + 1 == len(p):
                if sChars[ord(s[l]) - ord("a")] > 0:
                    sChars[ord(s[l]) - ord("a")] -= 1
                l += 1
        
        return res


            

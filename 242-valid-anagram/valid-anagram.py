class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sCount = [0] * 26
        tCount = [0] * 26

        for c in s:
            key = ord(c) - ord("a")
            sCount[key] += 1

        for c in t:
            key = ord(c) - ord("a")
            tCount[key] += 1

        
        return sCount == tCount

        
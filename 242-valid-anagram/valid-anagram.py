class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = [0] * 26, [0] * 26

        for char in s:
            idx = ord(char) - ord("a")
            sCount[idx] += 1
        
        for char in t:
            idx = ord(char) - ord("a")
            tCount[idx] += 1
        
        return sCount == tCount
        
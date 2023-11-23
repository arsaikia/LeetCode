class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charsCount = collections.defaultdict(int)

        for char in s:
            charsCount[ord(char)] += 1
        
        for char in t:
            charCode = ord(char)
            if charCode not in charsCount:
                return False
            
            if charsCount[charCode] == 0:
                return False
            
            if charsCount[charCode] == 1:
               charsCount.pop(charCode)
            else:
                charsCount[charCode] -= 1
        
        return len(charsCount) == 0
        
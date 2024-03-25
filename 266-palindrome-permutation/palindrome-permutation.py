class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        charCount = collections.defaultdict(int)
        for char in s:
            charCount[char] += 1
        
        isOddAllowed = len(s) % 2 == 1

        for val in charCount.values():
            if val % 2 == 1:
                if isOddAllowed:
                    isOddAllowed = False
                else:
                    return False
                

        return True


        
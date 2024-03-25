class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = [0] * 26
        for char in s:
            idx = ord(char) - ord("a")
            count[idx] += 1
        
        isOddAllowed = len(s) % 2 == 1

        for val in count:
            if val % 2 == 1:
                if isOddAllowed:
                    isOddAllowed = False
                else:
                    return False
                

        return True


        
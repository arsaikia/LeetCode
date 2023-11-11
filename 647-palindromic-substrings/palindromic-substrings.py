class Solution:
    def expandAndCheckPalindrome(self, s, l, r):
            palindromesCount = 0
            while l > -1 and r < len(s) and s[l] == s[r]:
                palindromesCount += 1
                l -= 1
                r += 1
            return palindromesCount

    def countSubstrings(self, s: str) -> int:
        numOfPalindromes = 0

        for idx in range(len(s)):
            
            # Get odd palindromes
            left, right = idx, idx
            numOfPalindromes += self.expandAndCheckPalindrome(s, left, right)

            # Get even palindromes
            left, right = idx, idx + 1
            numOfPalindromes += self.expandAndCheckPalindrome(s, left, right)
        
        return numOfPalindromes



        
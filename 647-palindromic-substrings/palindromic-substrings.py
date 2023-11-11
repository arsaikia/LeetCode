class Solution:
    def countSubstrings(self, s: str) -> int:

        def expandAndCheckPalindrome(st, l, r):
            palindromes = 0
            while l > -1 and r < len(st) and st[l] == st[r]:
                palindromes += 1
                l -= 1
                r += 1
            
            return palindromes
        

        numOfPalindromes = 0

        for idx in range(len(s)):
            
            # Get odd palindromes
            left, right = idx, idx
            numOfPalindromes += expandAndCheckPalindrome(s, left, right)

            # Get even palindromes
            left, right = idx, idx + 1
            numOfPalindromes += expandAndCheckPalindrome(s, left, right)
        
        return numOfPalindromes



        
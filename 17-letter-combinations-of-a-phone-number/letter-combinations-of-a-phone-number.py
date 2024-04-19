class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        
        alldigits = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        res = []

        def backtrack(i, comb):
            if len(comb) == len(digits):
                res.append("".join(comb[:]))
                return
            
            digit = alldigits[digits[i]]
            for letter in digit:
                comb.append(letter)
                backtrack(i + 1, comb)
                comb.pop()
            
        backtrack(0, [])
        return res
        

        
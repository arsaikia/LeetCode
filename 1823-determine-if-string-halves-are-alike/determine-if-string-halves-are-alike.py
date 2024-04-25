class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        def countVowel(start, end, s):
            answer = 0
            for i in range(start, end):
                if s[i] in "aieouAIEOU":
                    answer += 1
            return answer

        n = len(s)

        return countVowel(0, n//2, s) == countVowel(n//2, n, s)
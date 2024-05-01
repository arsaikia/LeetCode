class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1

        for i, c in enumerate(word):
            if c == ch:
                idx = i
                break
        
        if idx == -1:
            return word
        
        return word[: idx + 1][::-1] + word[idx + 1:]
        
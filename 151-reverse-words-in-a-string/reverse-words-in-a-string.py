class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(" ")
        word = s.split(" ")
        res = []
        for w in reversed(word):
            if w == "":
                continue
            res.append(w)
            res.append(" ")
        
        
        return "".join(res[:-1])
        
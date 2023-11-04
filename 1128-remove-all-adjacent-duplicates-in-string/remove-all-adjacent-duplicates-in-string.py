class Solution:
    def removeDuplicates(self, s: str) -> str:
        uniqueSoFar = []

        for ch in s:
            if uniqueSoFar:
                lastChar = uniqueSoFar[-1]
                if ch == lastChar:
                    uniqueSoFar.pop()
                    continue
            uniqueSoFar.append(ch)
        return "".join(uniqueSoFar)


        
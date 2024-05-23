class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS, stackT = [], []
        for ch in s:
            if ch == "#":
                if len(stackS):
                    stackS.pop()
            else:
                stackS.append(ch)
        
        for ch in t:
            if ch == "#":
                if len(stackT):
                    stackT.pop()
            else:
                stackT.append(ch)
        
        return stackS == stackT
        
        
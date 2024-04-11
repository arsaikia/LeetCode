class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        monotonicStack = []
        i = 0

        for ch in num:
            
            # if stack is empty do not add "0"
            if not len(monotonicStack) and ch == "0":
                continue

            # the top value on stack is greater than curr value
            while k > 0 and len(monotonicStack) and monotonicStack[-1] > ch:
                monotonicStack.pop()
                k -= 1
            
            monotonicStack.append(ch)
        
        if k > 0:
            monotonicStack = monotonicStack[ : len(monotonicStack) - k]
            k = 0
        
        i = 0
        while i < len(monotonicStack):
            if monotonicStack[i] != "0":
                break
            i += 1
        res = "".join(monotonicStack[i : ])


        return res if res else "0"

        


        
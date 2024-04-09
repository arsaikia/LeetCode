class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        l = k - 1
        r = k + 1
        val = tickets[k]
        res += val

        while l >= 0:
            left = tickets[l]
            if left >= val:
                res += val
            else:
                res += left
            l -= 1
        
        while r < len(tickets):
            right = tickets[r]
            if right >= val:
                res += val - 1
            else:
                res += right
            r += 1
        
        return res

        
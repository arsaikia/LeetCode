class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        recolors = 0
        globalRecolor = float("inf")

        for r in range(len(blocks)):
            if blocks[r] == "W":
                recolors += 1
            
            if r - l + 1 > k:
                if blocks[l] == "W":
                    recolors -= 1
                l += 1
            
            if r - l + 1 == k:
                globalRecolor = min(globalRecolor, recolors)
            
        return globalRecolor
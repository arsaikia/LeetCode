class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = []
        self.prefixSum = 0
        for weight in w:
            self.prefixSum += weight
            self.prefixSums.append(self.prefixSum)
        self.total = self.prefixSum

    def pickIndex(self) -> int:
        randomChoice = random.random() * self.total

        l, r = 0, len(self.prefixSums) - 1

        while l <= r:
            m = l + (r - l) // 2
            curr = self.prefixSums[m]
            if randomChoice == curr:
                return m
            elif randomChoice > curr:
                l = m + 1
            else:
                r = m - 1
        
        return l

            

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
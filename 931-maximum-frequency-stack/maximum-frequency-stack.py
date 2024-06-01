class FreqStack:

    def __init__(self):
        self.stacks = defaultdict(list)
        self.maxFreq = 0
        self.counts = defaultdict(int)

    def push(self, val: int) -> None:
        self.counts[val] += 1
        valCount = self.counts[val]

        if valCount > self.maxFreq:
            self.maxFreq = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxFreq].pop()
        self.counts[res] -= 1
        if not self.stacks[self.maxFreq]:
            self.maxFreq -= 1

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
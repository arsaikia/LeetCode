class FreqStack:

    def __init__(self):
        self.count = collections.defaultdict(int)
        self.maxCount = 0
        self.stacks = collections.defaultdict(list)
        

    def push(self, val: int) -> None:
        self.count[val] += 1
        count = self.count[val]
        if count > self.maxCount:
            self.maxCount = count
            self.stacks[count] = []
        self.stacks[count].append(val)
        

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.count[res] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1

        return res 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
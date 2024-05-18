class TimeMap:
    def __init__(self):
        self.keyStore = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore[key]

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + (r - l) // 2)
            __, ts = values[m]
            if ts <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
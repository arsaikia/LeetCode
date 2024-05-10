class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        factors = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                one, two = arr[i], arr[j]
                factors.append([one/two, one, two])
        factors.sort()
        res = factors[k - 1]
        return res[1:]
        
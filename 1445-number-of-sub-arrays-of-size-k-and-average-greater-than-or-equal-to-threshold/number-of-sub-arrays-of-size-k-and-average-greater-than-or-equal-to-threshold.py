class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        runningSum = 0
        subArrCount = 0

        for r in range(len(arr)):

            # close window
            if r - l + 1 > k:
                runningSum -= arr[l]
                l += 1

            # open window
            runningSum += arr[r]
            avg = runningSum // (r - l + 1)
            if r - l + 1 == k and avg >= threshold:
                subArrCount += 1
        
        return subArrCount


        
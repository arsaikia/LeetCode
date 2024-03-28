class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxSoFar = -1
        valueToRight = float("-inf")

        for idx in reversed(range(len(arr))):
            valueToRight = arr[idx]
            arr[idx] = maxSoFar
            maxSoFar = max(maxSoFar, valueToRight)
        
        return arr

        
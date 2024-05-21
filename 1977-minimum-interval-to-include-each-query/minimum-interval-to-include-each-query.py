class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort intervals
        intervals.sort()

        # sort queries, but keep original query idx

        minHeap = []
        res, i = {}, 0

        for q in sorted(queries):
            # if the curr q is after the interval start from left
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            # if the smallest in minHeap ends before q
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]


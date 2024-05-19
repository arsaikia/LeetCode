class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [ -1 * val for val in count.values() ]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #[val, timeWhenAvailable]

        while maxHeap or q:
            time += 1

            if maxHeap:
                val = heapq.heappop(maxHeap)
                nextCount = 1 + val
                if nextCount:
                    q.append( [nextCount, time + n] )  # when this item will be available next
                
            if q and q[0][1] == time:
                c, t = q.popleft()
                heapq.heappush(maxHeap, c )

        return time 
        
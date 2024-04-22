class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def findNext(node):
            direction = []
            for i in range(len(node)):
                prev = node[ : i]
                curr = node[i]
                nxt = node[i + 1 : ]
                if curr == "0":
                    direction.append(prev + "9" + nxt)
                    direction.append(prev + "1" + nxt)
                elif curr == "9":
                    direction.append(prev + "0" + nxt)
                    direction.append(prev + "8" + nxt)
                else:
                    direction.append(prev + str(int(curr) + 1) + nxt)
                    direction.append(prev + str(int(curr) - 1) + nxt)
            return direction

        deadends = set(deadends)
        visited = set()
        minSteps = 0

        # Perform BFS from staring node to get the target
        q = collections.deque(["0000"])

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return minSteps
                
                if curr in deadends or curr in visited:
                    continue
                
                visited.add(curr)

                for nextNode in findNext(curr):
                    q.append(nextNode)
    
            minSteps += 1
            
        return -1

            
            



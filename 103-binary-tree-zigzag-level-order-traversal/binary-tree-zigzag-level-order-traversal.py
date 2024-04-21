# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        res = []
        depth = 1

        while q:
            qSize = len(q)
            level = []

            for i in range(qSize):
                node = q.popleft()
                if not node:
                    continue
                
                level.append(node.val)
                
                q.append(node.left)
                q.append(node.right)
            if level:
                if depth % 2 == 0:
                    res.append(reversed(level))
                else:
                    res.append(level)
                
                depth += 1
                    
        return res




        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = collections.deque( [root] )
        lastNode = None

        while q:
            node = q.popleft()
            if not node:
                continue
            lastNode = node
            q.append(node.right)
            q.append(node.left)
        return lastNode.val
        
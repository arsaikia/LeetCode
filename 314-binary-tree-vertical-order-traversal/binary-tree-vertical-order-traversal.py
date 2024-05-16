# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#       [[9],[3,15],[20],[7]]
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            if root is None:
                return []

        colTable = collections.defaultdict(list)
        q = collections.deque([(root, 0)])   # (node, col)

        minCol, maxCol = 0, 0

        while q:
            node, col = q.popleft()

            if node is not None:
                colTable[col].append(node.val)

                minCol = min(minCol, col)
                maxCol = max(maxCol, col)

                q.append( (node.left, col - 1) )
                q.append( (node.right, col + 1) )
        
        return [colTable[key] for key in range(minCol, maxCol + 1)]


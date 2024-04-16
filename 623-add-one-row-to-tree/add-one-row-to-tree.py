# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        q = collections.deque([root])

        while depth > 2:
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth -= 1
        
        for __ in range(len(q)):
            curr = q.popleft()
            left = curr.left
            right = curr.right
            nextNode = TreeNode(val)
            
            new1 = TreeNode(val)
            new2 = TreeNode(val)

            curr.left = new1
            new1.left = left

            curr.right = new2
            new2.right = right

        return root
        
        return root


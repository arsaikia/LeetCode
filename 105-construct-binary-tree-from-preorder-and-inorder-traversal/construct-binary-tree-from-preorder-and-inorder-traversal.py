# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {val : idx for idx, val in enumerate(inorder)}
        rootIdx = 0


        def buildTreeHelper(l, r):
            nonlocal rootIdx
            
            if l > r:
                return None
            
            nodeVal = preorder[rootIdx]
            rootIdx += 1

            node = TreeNode(nodeVal)
            nodeIdxAtInorder = inorderIdx[nodeVal]

            node.left = buildTreeHelper(l, nodeIdxAtInorder - 1)
            node.right = buildTreeHelper(nodeIdxAtInorder + 1, r)
            return node
        
        return buildTreeHelper(0, len(inorder) - 1)
        
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # using iterative "inorder" traverse since we need to retreive the k-th smallest element
        res = []
        def inorder(node):
            # if there is no room for traverse:
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        # initiating the traversal
        inorder(root)
        return res[k-1]

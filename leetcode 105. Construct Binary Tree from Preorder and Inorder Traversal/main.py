# Definition for a binary tree node.
from typing import List, Optional


# objective of the problem:
#       to reconstruct the original binary tree structure from these GIVEN traversal arrays
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if nothing exist,
        if not preorder or not inorder:
            return None

        # first idx of the List (i.e., TreeNode) is ALWAYS root
        root_lst = TreeNode(preorder[0])
        # then, find index number by using the previously found value from the "inordered" tree
        mid_idx  = inorder.index(preorder[0])

        root_lst.left  = self.buildTree(preorder[1:mid_idx+1], inorder[:mid_idx])
        root_lst.right = self.buildTree(preorder[mid_idx+1:], inorder[mid_idx+1:])

        return root_lst


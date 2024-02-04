# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # case 1: if 'root' is existed, but has NOT subroot:
        if not subRoot:
            return True
        # case 2: if 'root' is empty but has subroot, which is logically error:
        if not root:
            return False

        # case main: if the offsprings (i.e., subtrees) are consecutively same, then return "True"
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, crnt_rt, sub_rt):
        # if both trees have NO child node (i.e., considered as IDENTICAL)
        if not crnt_rt and not sub_rt:
            return True

        # if one node has child node, but not the OTHER (i.e., considered as NOT identical)
        if not crnt_rt or not sub_rt:
            return False

        # check the detail of both sides (left and right sub tree), and checking them consecutively
        return crnt_rt.val == sub_rt.val and self.isSameTree(crnt_rt.left, sub_rt.left) \
            and self.isSameTree(crnt_rt.right, sub_rt.right)



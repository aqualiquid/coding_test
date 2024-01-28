# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.isHeight(root) >= 0)

    def isHeight(self, root):
        if root is None:
            return 0

        """
        left_h < 0:
            if subtree of the left is imbalanced
        right_h < 0:
            if subtree of the right is imbalanced
        abs(left_h - right_h) > 1 
            if different of the height is bigger than 1 (i.e., the tree is imbalanced)
        """
        left_h, right_h = self.isHeight(root.left), self.isHeight(root.right)
        if left_h < 0 or right_h < 0 or abs(left_h - right_h) > 1:
            return -1
        return max(left_h, right_h) + 1

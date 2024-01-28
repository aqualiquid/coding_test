# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        cnt = 0
        stack = [(root, root.val)]

        while stack:
            node, max_val = stack.pop()  # 마지막 요소를 제거 (스택)
            if node:
                if node.val >= max_val:
                    cnt += 1
                max_val = max(max_val, node.val)
                if node.left:
                    stack.append((node.left, max_val))
                if node.right:
                    stack.append((node.right, max_val))

        return cnt
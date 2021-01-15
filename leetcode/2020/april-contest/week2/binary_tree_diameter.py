# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def depth(self, node):
        if node is None:
            return (0, 0)

        left = depth(node.left)
        right = depth(node.right)
        d = max(left[0], right[0], left[1] + right[1])
        return (d, max(left[1], right[1]) + 1)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return depth(root)[0]

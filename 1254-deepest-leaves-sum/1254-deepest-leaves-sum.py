# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        self.res = 0
        def helper(root, depth):
            if root is None:
                return
            if depth == self.maxDepth:
                self.res += root.val
            elif depth > self.maxDepth:
                self.maxDepth = depth
                self.res = root.val
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return self.res
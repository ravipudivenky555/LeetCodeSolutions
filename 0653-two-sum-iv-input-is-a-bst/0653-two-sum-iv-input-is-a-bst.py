# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        flag = False
        def helper(node):
            nonlocal flag
            if not node:
                return
            if flag:
                return
            if (k - node.val) in nums:
                flag = True
                return
            nums.add(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(root)
        return flag
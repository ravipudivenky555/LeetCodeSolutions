# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        li = self.inorder(root, [])
        n = len(li)
        i, j = 1, n-2
        a = li[0]
        for i in range(1, n):
            if li[i].val < li[i-1].val:
                a = li[i-1]
                break
        b = li[-1]
        for i in range(n-2, -1, -1):
            if li[i].val > li[i+1].val:
                b = li[i+1]
                break
        a.val,b.val = b.val, a.val
    def inorder(self, root, li):
        if root is None:
            return li
        li = self.inorder(root.left, li)
        li.append(root)
        li = self.inorder(root.right, li)
        return li
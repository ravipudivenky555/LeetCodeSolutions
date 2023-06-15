# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=[root]
        q0=[]
        maxSum=root.val
        currLvl=1
        maxSumLvl=1
        while q:
            s=0
            while q:
                n=q.pop()
                if n.left:q0.append(n.left)
                if n.right:q0.append(n.right)
                s+=n.val
            q,q0=q0,q
            if s>maxSum:
                maxSum=s
                maxSumLvl=currLvl
            currLvl+=1
        return maxSumLvl
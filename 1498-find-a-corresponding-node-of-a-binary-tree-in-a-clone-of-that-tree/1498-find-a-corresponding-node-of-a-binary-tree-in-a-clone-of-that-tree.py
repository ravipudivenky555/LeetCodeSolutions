# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original==target:
            return cloned
        temp=original
        temp1=cloned
        stk1=[]
        stk2=[]
        while stk1 or temp:
            if temp:
                if temp==target:
                    return temp1
                stk1.append(temp)
                stk2.append(temp1)
                temp=temp.left
                temp1=temp1.left
            else:
                temp=stk1.pop()
                temp1=stk2.pop()
                if temp==target:
                    return temp1
                temp=temp.right
                temp1=temp1.right
        return None
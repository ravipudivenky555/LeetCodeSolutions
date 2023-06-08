# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n=0
        listStack=[]
        temp=head
        while temp!=None:
            n+=1
            temp=temp.next
        temp=head
        if n%2:
            for i in range(n):
                if i==int(n/2):
                    pass
                elif i<n/2:
                    listStack.append(temp)
                else:
                    if temp.val!=listStack.pop().val:
                        return False
                temp=temp.next
        else:
            for i in range(n):
                if i<n/2:
                    listStack.append(temp)
                else:
                    if temp.val!=listStack.pop().val:
                        return False
                temp=temp.next
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        t=head
        while t:
            if t in s:
                return True
            s.add(t)
            t=t.next
        return False
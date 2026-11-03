# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        rev = self.reverseList(slow.next)
        slow.next = None
        c = head
        c1 = rev
        while c1:
            n = c.next
            n1 = c1.next
            c.next = c1
            c1.next = n
            c = n
            c1 = n1

    def reverseList(self, head):
        d = None
        c = head
        while c:
            n = c.next
            c.next = d
            d = c
            c = n
        return d

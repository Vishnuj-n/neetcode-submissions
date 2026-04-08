# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split list
        sec = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp

        # merge two halves
        fir, sec = head, prev
        while sec:
            tmp1, tmp2 = fir.next, sec.next
            fir.next = sec
            sec.next = tmp1
            fir, sec = tmp1, tmp2
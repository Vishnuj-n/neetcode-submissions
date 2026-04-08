# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        tmp=head
        while tmp!=None:
            length+=1
            tmp=tmp.next   
        #delete length-n
        if n==length:
            return head.next
        place=length-n-1
        tmp=head
        for _ in range(place):
            tmp=tmp.next
        tmp.next=tmp.next.next
        return head 




        
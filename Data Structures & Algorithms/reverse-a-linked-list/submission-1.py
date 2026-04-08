class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev=head,None
        while curr:
            fur=curr.next
            curr.next=prev
            prev=curr
            curr=fur
        return prev
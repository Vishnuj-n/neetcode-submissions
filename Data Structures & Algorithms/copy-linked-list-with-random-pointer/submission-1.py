"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tmp=head
        mapping={}
        if not head:
            return None
        while tmp:
            mapping[tmp]=Node(tmp.val)
            tmp=tmp.next
        tmp=head
        while tmp:
            s1=mapping[tmp]
            s1.next = mapping.get(tmp.next)
            s1.random = mapping.get(tmp.random)
            tmp=tmp.next
        return mapping[head]
        





        



        
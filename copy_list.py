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
        if not head:
            return None
        mp={}
        curr=head
        while curr:
            mp[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            mp[curr].next=mp.get(curr.next)
            mp[curr].random=mp.get(curr.random)
            curr=curr.next
        return mp[head]
        
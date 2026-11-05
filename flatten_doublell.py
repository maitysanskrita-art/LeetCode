class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        stack = [head]
        prev = None

        while stack:
            curr = stack.pop()

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)

            if prev:
                prev.next = curr

            curr.prev = prev
            curr.child = None

            prev = curr

        prev.next = None
        head.prev = None

        return head
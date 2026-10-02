import random

class Solution:

    def __init__(self, head: ListNode | None):
        self.head = head

    def getRandom(self) -> int:
        current = self.head
        result = current.val
        count = 1

        while current:
            if random.randint(1, count) == 1:
                result = current.val

            current = current.next
            count += 1

        return result
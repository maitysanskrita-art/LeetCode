class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        return values == values[::-1]
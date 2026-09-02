class Solution:
    def kthSmallest(self, root, k):
        stack = []
        current = root

        while True:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Take the smallest remaining node
            current = stack.pop()
            k -= 1

            # If this is the kth node, return it
            if k == 0:
                return current.val

            # Now explore the right subtree
            current = current.right
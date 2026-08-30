class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = root
        right = root

        lh = 0
        rh = 0

        while left:
            lh += 1
            left = left.left

        while right:
            rh += 1
            right = right.right

        if lh == rh:
            return (2 ** lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
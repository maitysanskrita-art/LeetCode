     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left, right):
            # If both nodes are empty, they are symmetric
            if left is None and right is None:
                return True

            # If one node is empty and the other is not
            if left is None or right is None:
                return False

            # Values must be equal
            if left.val != right.val:
                return False

            # Compare opposite children
            return mirror(left.left, right.right) and mirror(left.right, right.left)

        return mirror(root.left, root.right)
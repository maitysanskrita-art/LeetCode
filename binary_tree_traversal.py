# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)      # Visit left subtree
            result.append(node.val) # Visit root
            inorder(node.right)     # Visit right subtree

        inorder(root)
        return result
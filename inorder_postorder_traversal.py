# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Store each value's index in inorder for quick lookup
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i

        # Recursive function to build the tree
        def helper(left, right):

            # No elements left in this subtree
            if left > right:
                return None

            # Last element of postorder is the root
            rootValue = postorder.pop()

            # Create the root node
            root = TreeNode(rootValue)

            # Find root position in inorder
            mid = index[rootValue]

            # Build right subtree first
            root.right = helper(mid + 1, right)

            # Build left subtree
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
        
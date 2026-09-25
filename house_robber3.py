class Solution:
    def rob(self, root: TreeNode | None) -> int:

        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            # If we rob this house
            rob = node.val + left[1] + right[1]

            # If we don't rob this house
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(dfs(root))
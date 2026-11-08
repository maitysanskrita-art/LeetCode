
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countFrom(node, target):
            if not node:
                return 0

            count = 1 if node.val == target else 0

            count += countFrom(node.left, target - node.val)
            count += countFrom(node.right, target - node.val)

            return count

        if not root:
            return 0

        return (countFrom(root, targetSum)
                + self.pathSum(root.left, targetSum)
                + self.pathSum(root.right, targetSum))

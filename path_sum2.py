 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result=[]
        def dfs(node,target,path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and target==node.val:
                result.append(path[:])
            else:
                dfs(node.left,target-node.val,path)
                dfs(node.right,target-node.val,path)
            path.pop()
        dfs(root,targetSum,[])
        return result
        
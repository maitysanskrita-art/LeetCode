class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]

        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                for child in node.children:
                    q.append(child)
            res.append(level)

        return res
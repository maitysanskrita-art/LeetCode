class Codec:

    def serialize(self, root):
        values = []

        def preorder(node):
            if not node:
                return
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(values)

    def deserialize(self, data):
        if not data:
            return None

        values = list(map(int, data.split(",")))
        index = 0

        def build(lower, upper):
            nonlocal index

            if index == len(values):
                return None

            val = values[index]

            if val < lower or val > upper:
                return None

            index += 1
            node = TreeNode(val)

            node.left = build(lower, val)
            node.right = build(val, upper)

            return node

        return build(float("-inf"), float("inf"))
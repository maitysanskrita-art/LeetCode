class Codec:

    def serialize(self, root):
        if root is None:
            return "N"

        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        values = data.split(",")
        self.i = 0

        def build():
            if values[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(values[self.i]))
            self.i += 1

            node.left = build()
            node.right = build()

            return node

        return build()
class Codec(object):

    def serialize(self, root):
        ans = []

        def dfs(node):
            if not node:
                ans.append("#")
                return

            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(ans)

    def deserialize(self, data):
        values = iter(data.split(","))

        def dfs():
            val = next(values)

            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
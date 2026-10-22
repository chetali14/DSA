class Solution(object):
    def buildTree(self, inorder, postorder):
        pos = {val: i for i, val in enumerate(inorder)}
        idx = len(postorder) - 1

        def build(left, right):
            nonlocal idx

            if left > right:
                return None

            val = postorder[idx]
            idx -= 1

            root = TreeNode(val)
            mid = pos[val]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
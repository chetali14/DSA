class Solution(object):
    def buildTree(self, preorder, inorder):
        pos = {val: i for i, val in enumerate(inorder)}
        idx = [0]

        def build(left, right):
            if left > right:
                return None

            val = preorder[idx[0]]
            idx[0] += 1

            root = TreeNode(val)
            mid = pos[val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
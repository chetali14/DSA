class Solution(object):
    def maxPathSum(self, root):
        ans = [float('-inf')]

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            ans[0] = max(ans[0], node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return ans[0]
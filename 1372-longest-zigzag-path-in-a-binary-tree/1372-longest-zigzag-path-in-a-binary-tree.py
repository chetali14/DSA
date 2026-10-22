class Solution(object):
    def longestZigZag(self, root):
        ans = [0]

        def dfs(node, left, right):
            if not node:
                return

            ans[0] = max(ans[0], left, right)

            dfs(node.left, 0, left + 1)
            dfs(node.right, right + 1, 0)

        dfs(root, 0, 0)
        return ans[0]
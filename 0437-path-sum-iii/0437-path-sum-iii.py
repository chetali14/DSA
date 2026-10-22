class Solution(object):
    def pathSum(self, root, targetSum):
        count = [0]
        prefix = {0: 1}

        def dfs(node, total):
            if not node:
                return

            total += node.val

            if total - targetSum in prefix:
                count[0] += prefix[total - targetSum]

            prefix[total] = prefix.get(total, 0) + 1

            dfs(node.left, total)
            dfs(node.right, total)

            prefix[total] -= 1

        dfs(root, 0)
        return count[0]
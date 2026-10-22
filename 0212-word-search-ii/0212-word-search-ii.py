class Solution(object):
    def findWords(self, board, words):
        trie = {}

        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node["#"] = word

        ans = []
        m, n = len(board), len(board[0])

        def dfs(i, j, node):
            c = board[i][j]

            if c not in node:
                return

            nxt = node[c]

            if "#" in nxt:
                ans.append(nxt["#"])
                del nxt["#"]

            board[i][j] = "#"

            if i > 0 and board[i-1][j] != "#":
                dfs(i-1, j, nxt)
            if i < m-1 and board[i+1][j] != "#":
                dfs(i+1, j, nxt)
            if j > 0 and board[i][j-1] != "#":
                dfs(i, j-1, nxt)
            if j < n-1 and board[i][j+1] != "#":
                dfs(i, j+1, nxt)

            board[i][j] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return ans
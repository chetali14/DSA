class Solution(object):
    def pacificAtlantic(self, heights):
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, seen):
            seen.add((r, c))

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in seen and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, seen)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)

        return [[r, c] for r in range(m) for c in range(n)
                if (r, c) in pacific and (r, c) in atlantic]
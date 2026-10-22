class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            pu = find(u)
            pv = find(v)

            if pu == pv:
                ans = [u, v]
            else:
                parent[pu] = pv

        return ans
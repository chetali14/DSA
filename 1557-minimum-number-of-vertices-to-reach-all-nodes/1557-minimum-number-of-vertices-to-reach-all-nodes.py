
class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        has_incoming = [False] * n

        for u, v in edges:
            has_incoming[v] = True

        result = []

        for i in range(n):
            if not has_incoming[i]:
                result.append(i)

        return result

class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] != -1:
                continue

            color[i] = 0
            q = [i]

            while q:
                node = q.pop(0)

                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        q.append(nei)
                    elif color[nei] == color[node]:
                        return False

        return True
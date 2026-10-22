class Solution(object):
    def eventualSafeNodes(self, graph):
        n = len(graph)
        degree = [len(graph[i]) for i in range(n)]
        rev = [[] for _ in range(n)]

        for i in range(n):
            for j in graph[i]:
                rev[j].append(i)

        q = []

        for i in range(n):
            if degree[i] == 0:
                q.append(i)

        safe = []

        while q:
            node = q.pop(0)
            safe.append(node)

            for prev in rev[node]:
                degree[prev] -= 1

                if degree[prev] == 0:
                    q.append(prev)

        return sorted(safe)
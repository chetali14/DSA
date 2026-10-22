class Solution(object):
    def findItinerary(self, tickets):
        graph = {}

        for a, b in tickets:
            graph.setdefault(a, []).append(b)

        for a in graph:
            graph[a].sort(reverse=True)

        ans = []

        def dfs(src):
            while graph.get(src):
                dst = graph[src].pop()
                dfs(dst)

            ans.append(src)

        dfs("JFK")
        return ans[::-1]
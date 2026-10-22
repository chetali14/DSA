from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        while q:
            course = q.popleft()
            count += 1

            for nxt in graph[course]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)

        return count == numCourses
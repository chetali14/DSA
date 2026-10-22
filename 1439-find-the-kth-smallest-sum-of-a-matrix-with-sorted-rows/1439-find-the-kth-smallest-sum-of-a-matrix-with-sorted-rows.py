class Solution(object):
    def kthSmallest(self, mat, k):
        import heapq

        sums = [0]

        for row in mat:
            heap = []
            for s in sums:
                for x in row:
                    heapq.heappush(heap, s + x)

            sums = heapq.nsmallest(k, heap)

        return sums[k - 1]
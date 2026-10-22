class Solution(object):
    def findKthLargest(self, nums, k):
        import heapq

        heap = []

        for x in nums:
            heapq.heappush(heap, x)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
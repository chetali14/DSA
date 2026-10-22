class Solution(object):
    def mergeKLists(self, lists):
        import heapq

        heap = []
        count = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1

        dummy = ListNode(0)
        cur = dummy

        while heap:
            val, _, node = heapq.heappop(heap)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1

        return dummy.next
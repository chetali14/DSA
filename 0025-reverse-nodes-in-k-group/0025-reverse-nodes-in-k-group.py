class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            end = prev

            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next

            start = prev.next
            nxt = end.next

            # Reverse k nodes
            p = start
            q = nxt

            while p != nxt:
                temp = p.next
                p.next = q
                q = p
                p = temp

            prev.next = end
            prev = start
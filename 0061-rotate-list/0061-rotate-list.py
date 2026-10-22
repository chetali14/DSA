class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        curr = head
        n = 1

        while curr.next:
            curr = curr.next
            n += 1

        k = k % n
        if k == 0:
            return head

        curr.next = head

        for _ in range(n - k):
            curr = curr.next

        new_head = curr.next
        curr.next = None

        return new_head
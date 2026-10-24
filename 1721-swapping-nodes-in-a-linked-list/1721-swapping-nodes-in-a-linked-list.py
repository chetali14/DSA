
class Solution:
    def swapNodes(self, head, k):
        first = head

        # Find the kth node from the beginning
        for _ in range(k - 1):
            first = first.next

        # Find the kth node from the end
        second = head
        current = first

        while current.next:
            current = current.next
            second = second.next

        # Swap their values
        first.val, second.val = second.val, first.val

        return head

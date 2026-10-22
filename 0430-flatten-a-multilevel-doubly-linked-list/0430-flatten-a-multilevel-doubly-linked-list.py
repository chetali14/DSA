class Solution(object):
    def flatten(self, head):
        if not head:
            return head

        def dfs(node):
            curr = node
            last = None

            while curr:
                nxt = curr.next

                if curr.child:
                    child = curr.child
                    child_last = dfs(child)

                    curr.next = child
                    child.prev = curr
                    curr.child = None

                    child_last.next = nxt

                    if nxt:
                        nxt.prev = child_last

                    last = child_last
                else:
                    last = curr

                curr = nxt

            return last

        dfs(head)
        return head
class Solution(object):
    def removeDuplicateLetters(self, s):
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        stack = []
        used = set()

        for c in s:
            count[c] -= 1

            if c in used:
                continue

            while stack and c < stack[-1] and count[stack[-1]] > 0:
                used.remove(stack.pop())

            stack.append(c)
            used.add(c)

        return ''.join(stack)
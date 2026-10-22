class Solution(object):
    def backspaceCompare(self, s, t):
        a = []
        b = []

        for ch in s:
            if ch == '#':
                if a:
                    a.pop()
            else:
                a.append(ch)

        for ch in t:
            if ch == '#':
                if b:
                    b.pop()
            else:
                b.append(ch)

        return a == b
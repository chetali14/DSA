
import random
import bisect

class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.prefix = []
        total = 0

        for a, b, x, y in rects:
            points = (x - a + 1) * (y - b + 1)
            total += points
            self.prefix.append(total)

        self.total = total

    def pick(self):
        r = random.randint(1, self.total)

        i = bisect.bisect_left(self.prefix, r)
        a, b, x, y = self.rects[i]

        before = self.prefix[i - 1] if i > 0 else 0
        offset = r - before - 1

        width = x - a + 1

        u = a + offset % width
        v = b + offset // width

        return [u, v]

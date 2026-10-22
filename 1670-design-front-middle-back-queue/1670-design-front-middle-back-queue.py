class FrontMiddleBackQueue(object):

    def __init__(self):
        self.q = []

    def pushFront(self, val):
        self.q.insert(0, val)

    def pushMiddle(self, val):
        self.q.insert(len(self.q) // 2, val)

    def pushBack(self, val):
        self.q.append(val)

    def popFront(self):
        if not self.q:
            return -1
        return self.q.pop(0)

    def popMiddle(self):
        if not self.q:
            return -1
        return self.q.pop((len(self.q) - 1) // 2)

    def popBack(self):
        if not self.q:
            return -1
        return self.q.pop()
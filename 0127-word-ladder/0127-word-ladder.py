class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return 0

        q = [(beginWord, 1)]
        seen = {beginWord}

        while q:
            word, steps = q.pop(0)

            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new = word[:i] + c + word[i+1:]

                    if new in words and new not in seen:
                        seen.add(new)
                        q.append((new, steps + 1))

        return 0
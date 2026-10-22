class Solution(object):
    def longestPalindrome(self, s):
        start = 0
        end = 0

        for i in range(len(s)):
            l = r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > end - start:
                    start = l
                    end = r
                l -= 1
                r += 1

            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > end - start:
                    start = l
                    end = r
                l -= 1
                r += 1

        return s[start:end + 1]
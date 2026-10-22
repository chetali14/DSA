from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        maxq = deque()
        minq = deque()
        left = 0
        ans = 0

        for right in range(len(nums)):
            while maxq and nums[maxq[-1]] < nums[right]:
                maxq.pop()
            maxq.append(right)

            while minq and nums[minq[-1]] > nums[right]:
                minq.pop()
            minq.append(right)

            while nums[maxq[0]] - nums[minq[0]] > limit:
                if maxq[0] == left:
                    maxq.popleft()
                if minq[0] == left:
                    minq.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans
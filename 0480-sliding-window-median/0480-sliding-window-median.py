class Solution(object):
    def medianSlidingWindow(self, nums, k):
        import bisect

        window = sorted(nums[:k])
        ans = []

        for i in range(k, len(nums) + 1):
            if k % 2:
                ans.append(float(window[k // 2]))
            else:
                ans.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

            if i == len(nums):
                break

            old = nums[i - k]
            pos = bisect.bisect_left(window, old)
            window.pop(pos)

            bisect.insort(window, nums[i])

        return ans
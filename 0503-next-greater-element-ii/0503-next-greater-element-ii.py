class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                ans[stack.pop()] = nums[i % n]

            if i < n:
                stack.append(i)

        return ans
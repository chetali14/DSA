class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        for x in nums:
            i = abs(x) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]

        ans = []

        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans
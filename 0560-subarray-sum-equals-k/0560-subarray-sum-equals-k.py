class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        total = 0
        prefix = {0: 1}

        for num in nums:
            total += num

            if total - k in prefix:
                count += prefix[total - k]

            prefix[total] = prefix.get(total, 0) + 1

        return count
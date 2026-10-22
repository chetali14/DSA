class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        def merge_sort(a):
            if len(a) <= 1:
                return 0

            mid = len(a) // 2
            left = a[:mid]
            right = a[mid:]

            count = merge_sort(left) + merge_sort(right)

            j = k = 0
            for x in left:
                while j < len(right) and right[j] - x < lower:
                    j += 1
                while k < len(right) and right[k] - x <= upper:
                    k += 1
                count += k - j

            a[:] = sorted(left + right)
            return count

        return merge_sort(prefix)
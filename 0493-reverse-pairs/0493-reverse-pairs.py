class Solution(object):
    def reversePairs(self, nums):
        def merge_sort(a):
            if len(a) <= 1:
                return 0

            mid = len(a) // 2
            left = a[:mid]
            right = a[mid:]

            count = merge_sort(left) + merge_sort(right)

            j = 0
            for x in left:
                while j < len(right) and x > 2 * right[j]:
                    j += 1
                count += j

            a[:] = sorted(left + right)
            return count

        return merge_sort(nums)
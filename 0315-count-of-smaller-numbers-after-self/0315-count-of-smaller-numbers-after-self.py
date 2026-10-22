class Solution(object):
    def countSmaller(self, nums):
        n = len(nums)
        ans = [0] * n
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(a):
            if len(a) <= 1:
                return a

            mid = len(a) // 2
            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:])

            i = j = 0
            merged = []

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    ans[left[i][1]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                ans[left[i][1]] += j
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(arr)
        return ans
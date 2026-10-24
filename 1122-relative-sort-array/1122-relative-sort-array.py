
class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = {}

        # Count occurrences of each number
        for num in arr1:
            count[num] = count.get(num, 0) + 1

        result = []

        # Add numbers in the order given by arr2
        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0

        # Add remaining numbers in ascending order
        for num in sorted(count):
            result.extend([num] * count[num])

        return result

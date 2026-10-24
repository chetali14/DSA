
class Solution:
    def arrayRankTransform(self, arr):
        sorted_nums = sorted(set(arr))
        rank = {}

        # Assign a rank to each unique number
        for i, num in enumerate(sorted_nums):
            rank[num] = i + 1

        # Replace each number with its rank
        return [rank[num] for num in arr]

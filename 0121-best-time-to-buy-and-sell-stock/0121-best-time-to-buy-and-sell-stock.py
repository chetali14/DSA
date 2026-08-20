class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p= float(inf)
        max_p= 0
        for i in prices:     
            min_p = min(min_p, i)
            max_p = max(max_p, i - min_p)
        return max_p        
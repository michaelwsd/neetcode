class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for i, p in enumerate(prices):
            if p < prices[l]:
                l = i
            
            res = max(res, p - prices[l])

        return res
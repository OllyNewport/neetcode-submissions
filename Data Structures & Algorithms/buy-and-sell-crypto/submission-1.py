class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        current = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r                                   # new cheapest buy day
            else:
                current = max(current, prices[r] - prices[l])
            r += 1                                      # always advance

        return current
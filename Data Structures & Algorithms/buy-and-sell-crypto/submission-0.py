class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        l = 0
        r = l +1

        while r < len(prices):
            best = max(best, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                r += 1

        return best
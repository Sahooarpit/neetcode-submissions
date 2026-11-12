class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currMax = 0
        bestPrice = 0

        l, r = prices[0], 0

        for i in prices:

            l = min(l, i)
            bestPrice = max(i-l, bestPrice)
        
        return bestPrice

            
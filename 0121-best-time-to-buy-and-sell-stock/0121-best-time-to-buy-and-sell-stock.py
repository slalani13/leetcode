class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            currPrice = prices[i]
            profit = currPrice - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit
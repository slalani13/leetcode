class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        currProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > minPrice:
                currProfit = prices[i] - minPrice
                maxProfit = max(currProfit, maxProfit)
            if prices[i] < minPrice:
                minPrice = prices[i]
        return maxProfit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        biggest_profit = 0
        cheapest_buying_price = float('inf')
        for i in range(1, len(prices)):
            cheapest_buying_price = min(cheapest_buying_price, prices[i-1])
            profit = prices[i] - cheapest_buying_price
            biggest_profit = max(biggest_profit, profit)
        return biggest_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        max_price = 0
        min_buy_price = prices[0]

        for sell_price in prices:
            price = sell_price - min_buy_price
            max_price = max(max_price, price)
            min_buy_price = min(min_buy_price, sell_price)
        return max_price

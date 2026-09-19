class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        if n <= 1:
            return 0

        buy = -prices[0]
        sell = 0
        cooldown = 0

        for i in range(1, n):
            old_buy = buy
            old_sell = sell

            buy = max(old_buy, cooldown - prices[i])
            sell = max(old_sell, old_buy + prices[i])
            cooldown = old_sell

        return sell
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        maxprofit=0
        for price in prices:
            if price<minprice:
                minprice=price
            else:
                maxprofit=max(maxprofit,price-minprice)
        return maxprofit
        
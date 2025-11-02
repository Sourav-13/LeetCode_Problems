class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ini_price = prices[0]
        profit =0
        for price in prices[1:]:
            if ini_price > price:
                ini_price = price
            
            if profit <  price - ini_price:
                profit = price - ini_price
        return profit
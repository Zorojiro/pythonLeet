class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        pro = 0

        for i in prices:
            if i < buy:
                buy = i
            elif i - buy > pro:
                pro = i - buy
        
        return pro
        
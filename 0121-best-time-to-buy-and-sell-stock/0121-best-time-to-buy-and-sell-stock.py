class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            profit = max(profit , prices[i] - minprice)
        
        return profit

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        max_profile = 0
        for price in prices:
            buy = min(buy, price)
            max_profile = max(max_profile, price-buy)
        return max_profile


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))
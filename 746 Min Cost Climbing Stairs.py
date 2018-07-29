class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        start_0 = 0
        start_1 = 0
        for each in cost[::-1]:
            old_start_1 = start_1
            start_1 = start_0
            start_0 = min(start_0 + each, old_start_1 + each)
        return min(start_0, start_1)


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    solution = Solution()
    print(solution.minCostClimbingStairs(cost))
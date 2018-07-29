class Solution1:
    """
    递归做法
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution2:
    """
    非递归做法
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre_1_step = 1
        pre_2_step = 0
        count = 1
        for i in range(1, n+1):
            count = pre_1_step + pre_2_step
            pre_2_step = pre_1_step
            pre_1_step = count
        return count

class Solution:
    """
    非递归做法
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        F = [0, 1]
        count = 1
        for i in range(n):
            count = F[0] + F[1]
            F[0] = F[1]
            F[1] = count
        return count



if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(5))
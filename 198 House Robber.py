class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = best = 0
        for each in nums:
            pre_left = left
            left = best
            best = max(left, each + pre_left)
        return best


if __name__ == '__main__':
    nums = [2,7,9,3,1]
    solution = Solution()
    print(solution.rob(nums))

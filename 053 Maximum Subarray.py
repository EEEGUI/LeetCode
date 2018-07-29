class Solution1:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = -1*float('inf')
        best = -1*float('inf')
        result = -1*float('inf')
        for elem in nums:
            right = max(elem, elem + right)
            best = max(elem, best)
            best = max(right, best)
            if best > result:
                result = best
        return result


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]
        sum = 0
        for elem in nums:
            if sum >= 0:
                sum += elem
                max_val = max(max_val, sum)
            else:
                sum = elem
                max_val = max(max_val, sum)
        return max_val

if __name__ == '__main__':
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(nums))
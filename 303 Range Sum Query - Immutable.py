class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.accu_sum = self.cal_accu_sum()

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu_sum[j] - self.accu_sum[i] + self.nums[i]

    def cal_accu_sum(self):
        """
        计算累积和
        :return:
        """
        accu_sum = []
        curren_sum = 0
        for each in self.nums:
            curren_sum += each
            accu_sum.append(curren_sum)
        return accu_sum
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        count = 0
        available = list(range(1, n))

        while True:
            new_available = []
            for i in available:
                if i < n - 1 and A[i + 1] + A[i - 1] == 2 * A[i]:
                    new_available.append(i+1)
                    count += 1
            available = new_available
            if len(available) == 0:
                break
        return count

if __name__ == '__main__':
    A = [1, 2, 3, 7, 4, 5, 6]
    s = Solution()
    print(s.numberOfArithmeticSlices(A))
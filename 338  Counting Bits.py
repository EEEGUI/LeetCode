class Solution1:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        count = [0] * (num + 1)
        exp = 0
        for i in range(1, num+1):
            if i == 2 ** exp:
                count[i] = 1
                exp += 1
            else:
                count[i] = count[2 ** (exp-1)] + count[i - 2 ** (exp-1)]
        return count

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        count = [0] * (num + 1)
        a = 1
        for i in range(1, num+1):
            if i == a:
                count[i] = 1
                a *= 2
            else:
                count[i] = count[a//2] + count[i - a//2]
        return count


if __name__ == '__main__':
    so = Solution()
    print(so.countBits(8))

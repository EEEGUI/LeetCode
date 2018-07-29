# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        queue = [(root, 0)]
        count = 0
        sum_ = 0
        current_level = 0

        while len(queue) > 0:
            node, level = queue.pop(0)
            if level > current_level:
                result.append(sum_/count)
                current_level += 1
                sum_ = 0
                count = 0
            if node:
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
                sum_ += node.val
                count += 1
        return result


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        level = [root]
        next_level = []
        total = 0
        while level:
            for i in range(len(level)):
                node = level[i]
                total += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(total/len(level))

            level = next_level
            total = 0
            next_level = []
        return result


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        level = [root]
        next_level = []
        total = 0
        while level:
            size = len(level)
            while level:
                node = level.pop()
                total += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(total/size)

            level = next_level
            total = 0
            next_level = []
        return result




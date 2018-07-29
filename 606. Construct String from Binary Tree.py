class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        ans = ''
        if not t:
            return ''
        stack = [t]
        while stack:
            node = stack.pop()
            while node:
                ans += str(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left
        return ans

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        if not t.left and t.right:
            return str(t.val) + '()' + '(' + str(self.tree2str(t.right)) + ')'
        elif t.left and not t.right:
            return str(t.val) + '(' + str(self.tree2str(t.left)) + ')'
        elif not t.left and not t.right:
            return str(t.val)
        else:
            return str(t.val) + '(' + str(self.tree2str(t.left)) + ')' + '(' + str(self.tree2str(t.right)) + ')'


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        elif t1 is None and t2:
            root = t2
            return root
        elif t2 is None and t1:
            root = t1
            return root
        else:
            return None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not (t1 is not None and t2 is not None):
            return t1 or t2
        else:
            queue = [(t1, t2, None, 0)]
            while len(queue) > 0:
                node_l, node_r, parent, is_left = queue.pop(0)
                if node_l and node_r:
                    node_l.val = node_l.val + node_r.val
                    queue.append((node_l.left, node_r.left, node_l, 1))
                    queue.append((node_l.right, node_r.right, node_l, 0))
                elif node_r:
                    if is_left:
                        parent.left = node_r
                    else:
                        parent.right = node_r
        return t1



class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(t):
    queue = [t]
    while len(queue) > 0:
        t = queue.pop(0)
        if t is None:
            print(t, end=' ')
        else:
            a = t.val
            print(t.val, end=' ')
            queue.append(t.left)
            queue.append(t.right)


if __name__ == '__main__':
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    print_tree(t1)

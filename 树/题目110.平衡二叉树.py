
'''

    给定一个二叉树，判断它是否是高度平衡的二叉树。

    本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。


'''


# 一道考研时候 刷过的题吧， 直接通过计算左右两侧的高度进行递归判别即可
# 时间复杂度为O(NlogN)，空间复杂度为O(log(N))
class Solution(object):
    #  获取平衡上 衡量的结果
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            # 满足平衡二叉树的条件，一方面必须是 左右深度差小些，另外就是左右都是平衡二叉树
            return abs(self.deep(root.left) - self.deep(root.right)) <= 1 and self.isBalanced(
                root.left) and self.isBalanced(root.right)

    def deep(self, root):
        if not root:
            return 0
        else:
            left = self.deep(root.left) + 1
            right = self.deep(root.right) + 1
            return max(left, right)
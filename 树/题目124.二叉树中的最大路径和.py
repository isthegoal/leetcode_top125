# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：
        给定一个非空二叉树，返回其最大路径和。本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，
        且不一定经过根节点。

        示例 1:

            输入: [1,2,3]

                   1
                  / \
                 2   3

            输出: 6

        示例 2:

            输入: [-10,9,20,null,null,15,7]

               -10
               / \
              9  20
                /  \
               15   7

            输出:  15+20+7 = 42


     分析：

     解法：

     现在万事俱备，只欠算法。

        1.初始化 max_sum 为最小可能的整数并调用函数 max_gain(node = root)。
        2.实现 max_gain(node) 检查是继续旧路径还是开始新路径：

             (1)边界情况：如果节点为空，那么最大权值是 0 。
             (2)对该节点的所有孩子递归调用 max_gain，计算从左右子树的最大权值：left_gain = max(max_gain(node.left), 0) 和 right_gain = max(max_gain(node.right), 0)。
             (3)检查是维护旧路径还是创建新路径。创建新路径的权值是：price_newpath = node.val + left_gain + right_gain，当新路径更好的时候更新 max_sum。
             (4)对于递归返回的到当前节点的一条最大路径，计算结果为：node.val + max(left_gain, right_gain)。

'''


class Solution:
    res = float('-inf')

    #  启动函数
    def maxPathSum(self, root):
        self.getMax(root)
        return self.res

    #  核心的  最大路径计算过程。
    def getMax(self, root):
        # 查找的边界条件   (1)
        if not root:
            return 0

        # 如果子树路径和为负则应当置0表示最大路径不包含子树   (2)
        left = max(0, self.getMax(root.left))
        right = max(0, self.getMax(root.right))

        # 以当前节点为根节点,判断在该节点包含左右子树的路径和是否大于当前最大路径和   (3)
        self.res = max(self.res, root.val + left + right)

        # 当前节点作为父节点的一个子节点和父节点连接的话则需取【单端的最大值】返回   (4)
        return max(left, right) + root.val
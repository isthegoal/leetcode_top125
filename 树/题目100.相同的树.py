

'''
     题目：给定两个二叉树，编写一个函数来检验它们是否相同。
           如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

     思路：这里使用递归的方式，不断进行 左右判断比较即可

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  思考较为简单： 直接使用递归的方式，不断进行 左右判断比较即可
#   时间复杂度为O(N)
#   最优情况（完全平衡二叉树）时为?O(log(N))，最坏情况下（完全不平衡二叉树）时为O(N)，用于维护递归栈。
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #递归停止条件
        if not p and not q:
            return True
        #通过的左右判别，迭代设置点
        elif p is not None and q is not None:
            if p.val==q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:
                return False
        #无效的 情况
        else:
            return False
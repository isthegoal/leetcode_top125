# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

   你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的
    节点将直接作为新二叉树的节点。

        示例 1:

        输入:
            Tree 1                     Tree 2
                  1                         2
                 / \                       / \
                3   2                     1   3
               /                           \   \
              5                             4   7
        输出:
        合并后的树:
                 3
                / \
               4   5
              / \   \
	         5   4   7


      分析：


      思路：考虑当两个结点合并时，如果这两个结点都存在，那么直接值相加，如果有一个不存在，直接返回另一个就好了。

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

#___________________________________    练习1   ______________________________#
#   这里合并非常简单，就是对应位置相加就可以了， 所以只需要非常简单的   先序遍历， 并不断累加即可，将和附加到一个树上。
def fun(t1,t2):
    # 两种边界条件, 比较重要的，  会遇到一个树的指向空了的情况，那直接 嫁接即可。
    if not t1:
        return t2
    if not t2:
        return t1

    # 主要操作： 进行结点的  加和
    t1.val+=t2.val

    #  加下来就是启动递归操作即可  (同步的递归 找相同位置的点)
    t1.left=fun(t1.left,t2.left)
    t1.right=fun(t1.right,t2.right)


    # 最后合到的是t1这个载体上即可
    return t1
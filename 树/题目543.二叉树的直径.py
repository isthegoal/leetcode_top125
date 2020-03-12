# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过
      根结点。

            示例 :
            给定二叉树

                  1
                 / \
                2   3
               / \
              4   5


            返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。    4走到3共走了三步，所以直径为3
            注意：两结点之间的路径长度是以它们之间边的数目表示。



      分析：


      思路：二叉树的直径：二叉树中从一个结点到另一个节点最长的路径，叫做二叉树的直径
            采用分治和递归的思想：根节点为root的二叉树的直径 = max(root-left的直径，root->right的直径，
            root->left的最大深度+root->right的最大深度+1)

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.ans

#___________________________________    练习1   ______________________________#
'''
   递归 实现把，基本就一点思路：
        根节点为root的二叉树的直径 = max(root-left的直径，root->right的直径，root->left的最大深度+root->right的最大深度+1)
   
   
   下面的 解题方式中，最核心的中间件是  左子树的最大深度  和 右子树的最大深度， 以最大深度为核心铺件。
   
       函数放回的是 当前结点root下 其左孩子最大深度和右孩子最大深度 对比下来的较大值。  
       
       通过这样不断的由下往上的dfs统计，就可以获得 每个结点的 左孩子最大深度和右孩子最大深度【最大深度是指 其下面孩子的深度】。
'''


class Solution1(object):
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #  内部首先dfs深度遍历，由下往上  进行递归
        self.dfs(root)

        return self.ans

    def dfs(self, root):
        # 递归截止条件, 到达根节点位置
        if not root:
            return 0

        #  这里获取的是   左子树中  最大的深度   和  右子树往下的最大深度
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        # 比较统计获取最大的直径，进行保存。
        self.ans = max(self.ans, left + right)

        # 最后  返回现在的  孩子的最大深度   +1
        return max(left, right) + 1
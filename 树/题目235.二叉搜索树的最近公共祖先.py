# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
            百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先
            且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
            例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

            示例 1:
            输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
            输出: 6
            解释: 节点 2 和节点 8 的最近公共祖先是 6。

            示例 2:
            输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
            输出: 2
            解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。



      分析：
           意思是  从给定的树root  中，找到 结点p和结点q的  最近公共祖先。

           这里 有个性质是  二叉搜索树： 因此左边都要比根小，右边都比根大。

      思路：这里主要还是使用  二叉搜索树的性质吧。
               根据性质往上判别。

           核心思路：
              利用二叉搜索树的特点。
              【1】如果p、q的值都小于root，说明p q 肯定在root的左子树中；
              【2】如果p q都大于root，说明肯定在root的右子树中，
              【3】如果一个在左一个在右 则说明此时的root记为对应的最近公共祖先


'''

#___________________________________    练习1   ______________________________#
#  有两种解法吧，递归解法  和  非递归解法
#  这里简单用 递归解决吧，进行寻找

# 利用二叉搜索树  的性质，找到左边小于、右边大于的结点，就是所需要的 最近公共结点
#  时间复杂度O(N)，空间复杂度O(N)
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root



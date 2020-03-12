# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：翻转一棵二叉树。  左右翻转的那种，比较简单

            示例：

            输入：

                 4
               /   \
              2     7
             / \   / \
            1   3 6   9
            输出：

                 4
               /   \
              7     2
             / \   / \
            9   6 3   1

      分析：


      思路：直接使用递归方式即可，  不过注意备份一下root.left 和root.right，因为会被覆盖

'''
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root



#___________________________________    练习1   ______________________________#
#  直接在递归中进行翻转   由下往上进行调整
#  时间复杂度为O(N)   空间复杂度为O(N)
class Solution1(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #边界条件
        if not root:
            return root

        #  四步把，实现递归的翻转，让其左指针 指向  递归下来处理好的左边，  右指针同理。  通过这样的方式实现完整的翻转操作.....
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)

        return root
# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点
      值加上所有大于它的节点值之和。

        例如：
        输入: 二叉搜索树:
                      5
                    /   \
                   2     13

        输出: 转换为累加树:
                     18
                    /   \
                  20     13

      分析：


      思路：有两种思路吧
        【1】先得到中序遍历，然后得到整个树的结点值的和，接着再遍历一次树，对每个节点加上 整个树的和 - 它自身和左子树之和。
        这种方法比较慢。
        【2】直接按照右中左的顺序中序遍历整棵树，用一个变量s记录下需要加的值。

'''

#思路一
class Solution1(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 每个节点应该加上整个树的和 减去 它自身和左子树之和
        if root is None:
            return None

        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)

        inorder = inOrder(root)

        dp = [0 for _ in range(len(inorder))]
        dp[0] = inorder[0]

        treesum = sum(inorder)
        for i in range(1, len(dp)):
            dp[i] = inorder[i] + dp[i - 1]

        def change(node):
            if not node:
                return

            pos = inorder.index(node.val)
            node.val += treesum - dp[pos]
            change(node.left)
            change(node.right)

        change(root)
        return root


#思路二
class Solution2(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 右中左的遍历顺序
        if not root:
            return root
        self.s = 0

        def convert(node):
            if not node:
                return

            convert(node.right)
            node.val += self.s
            self.s = node.val
            convert(node.left)

        convert(root)
        return root
# ___________________________________    练习1   ______________________________#
'''
    这里主要开始于两点， 分别是二叉搜索树的性质（左边小于、右边大于）、累加树（每个点都是大于的和，那就是右子树的和）的性质。
    以两个性质出发，感觉比较直观的方法就是  右中左这样的遍历方式，在这过程中，可以有效的记录计算出每个点的累加值，得到最后的累加树

    对于该思路，使用递归的方式进行实现。
    实现方式：按照右中左的顺序中序遍历整棵树，用一个变量s记录下需要加的值（这样每个位置，只需要添加上之前累加的s即可，能够很好地表示 加上了比它大的值）。
'''

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #  构建类内全局变量，省的穿起来费事。
        self.cur=0
        # 大的 二叉树的边界条件
        if not root:
            return root

        # 开始持续的  从右中左  这样的顺序开始，不断 进行累加到s,然后持续循环下去
        def convert(node):
            #  搜索下的截止条件
            if not node:
                return

            # 进行核心的 右中左的过程   node附加累加， s持续累加
            convert(node.right)
            node.val+=self.cur
            self.cur=node.val
            convert(node.left)

        # s符号是核心，是 不断收集的累加值，从右边开始累加。   那么由右往左的过程中，每个位置点其实只需要加上这个累加值s即可。
        convert(root)
        return root







# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉树，判断其是否是一个有效的二叉搜索树。

      假设一个二叉搜索树具有如下特征：
        节点的左子树只包含小于当前节点的数。
        节点的右子树只包含大于当前节点的数。
        所有左子树和右子树自身必须也是二叉搜索树。


        输入:
            2
           / \
          1   3
        输出: true


        输入:
            5
           / \
          1   4
             / \
            3   6
        输出: false
       解释: 输入为: [5,1,4,null,null,3,6]。
       根节点的值为 5 ，但是其右子节点值为 4 。

      分析：   很明显的，主要是要满足三点情况。
                          左右子树必须是二叉搜索树，  且  左子树结点都小于父节点、右子树结点大于父节点。

      思路：   感觉很明显的使用  中序遍历的方式即可， 进行中序的收集，
               这样收集下来的顺序，就会使越来越大的情况。

'''

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = list()
        self.inorderTra(root, inorder)
        # print inorder
        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]:
                return False
        return True

    def inorderTra(self, root, inorder):
        if not root:
            return None

        self.inorderTra(root.left, inorder)
        inorder.append(root.val)
        self.inorderTra(root.right, inorder)

        return

#___________________________________    练习1   ______________________________#
# 基本思路     是首先inorderTra进行先序收集， 之后对收集的结点进行 二叉搜索有效性上的检验。
# 时间复杂度为O(N)   空间复杂度为O(N)
def fun1(root):
    #  启动 大的遍历操作
    inorder=list()
    #  进行包纳库的收集
    fun2(root,inorder)

    #  从根节点的启动 收集结束后，  对收集的结果进行  子节点与父节点  数值比较关系上的判定
    #  根据 如上的收集方式，正确的大小比对关系  应如下。
    for i in range(len(inorder)-1):
        # 应该是 后比 前面大
        if inorder[i]>=inorder[i+1]:
            return False


    #最后  没问题的话，说明判别成功
    return True


# 这里传递的inorder  是收藏包纳库  （先序收集）    收集为【1  2   3】
def fun2(root,inorder):
    # 边界条件
    if not root:
        return None

    # 启动  类似中序的 收集方式
    fun2(root.left,inorder)

    #  中间位置上的收集。  上面走的都比它小，下面的都比它大。
    inorder.append(root.val)

    fun2(root.right,inorder)

    return

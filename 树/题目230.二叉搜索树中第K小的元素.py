# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

            说明：
            你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

            示例 1:

            输入: root = [3,1,4,null,2], k = 1
               3
              / \
             1   4
              \
               2
            输出: 1
            示例 2:

            输入: root = [5,3,6,2,4,null,null,1], k = 3
                   5
                  / \
                 3   6
                / \
               2   4
              /
             1
            输出: 3
            进阶：
            如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？


      分析：   感觉照着 搜索二叉树的性质，去寻找第k个小的元素，方式还是比较简单的。
               【1】一种比较简单的方法是  使用中序遍历的方式，获得序列，然后根据序列的次序关系 找到第k小的数值是哪个。
                      在这里不需要把所有的数字都遍历完，只需要遍历到第k个数字就行。

      思路：

'''
# 进行 中序遍历，  获取第k个遍历的值即可，不需要完全的遍历。   这里使用递归的方式实现中序遍历
# 时间复杂度为O(k),空间复杂度为O(N)
class Solution(object):
    def __init__(self):
        self.iter_num=0
        self.res=None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #  边界条件判别
        if not root:
            return
        #  左子树递归
        self.kthSmallest(root.left,k)

        #  中间位置的判别 和 计算。  中序遍历的判别计算部分
        self.iter_num+=1
        if self.iter_num==k:
            self.res=root.val

        # 比较核心的，进行k步即可，如果已经找到了，就不需要后面的递归查找了。
        else:
            #右子树递归
            self.kthSmallest(root.right,k)
        return self.res

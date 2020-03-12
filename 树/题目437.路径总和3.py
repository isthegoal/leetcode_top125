#

'''
     题目：
        给定一个二叉树，它的每个结点都存放着一个整数值。找出路径和等于给定数值的路径总数。
        路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
        二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

        示例：
            root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

                  10
                 /  \
                5   -3
               / \    \
              3   2   11
             / \   \
            3  -2   1

            返回 3。和等于 8 的路径有:

            1.  5 -> 3
            2.  5 -> 2 -> 1
            3.  -3 -> 11

     分析：
          这题 是  获取子路径的问题，可以在任意的结点结束，只要满足 子路径之和为  需要的num  即可。

         很容易就能想出一些  递归的思路，在递归中 更多未知进行  sum值 满足情况判别即可。

'''

#方法一. 递归方式  （当然可以非递归解法，但是递归解法更为直观）

#  比较容易理解的是使用  双重递归解法，按sum差值  去 DFS 遍历判别即可。   但是要顾虑好从每个位置可以作为开始和结尾，所以要双重形式
#  时间复杂度为O(n^2)   空间复杂度最优为O(n^2)
class Solution(object):
    def pathSum(self, root, sum):
        if root == None:
            return 0

        #  这个是双重 递归的形式， 一方面是当前结点启动，另一方面是对于其孩子 也分别启动递归。
        return self.count(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def count(self, root, sum):
        if root == None:
            return 0

        # 直接的  余值判别，   如果余值对应  那就满足条件了,满足条件路径+1。    (当前满足条件后，还得继续走 ，因为还可以以当前为起点，进行往下查找路径。  所以是个多重的形式)
        return int(root.val == sum) + self.count(root.left, sum - root.val) + self.count(root.right, sum - root.val)
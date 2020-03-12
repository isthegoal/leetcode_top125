# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给出一颗二叉树以及一个数字sum,判断这可二叉树上存在多少条路径，其路径上的所有结点和为sum.

              例如 root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

                      10
                     /  \
                    5   -3
                   / \    \
                  3   2   11
                 / \   \
                3  -2   1

                Return 3. The paths that sum to 8 are:

                1.  5 -> 3
                2.  5 -> 2 -> 1
                3. -3 -> 11


      分析：


      思路：首先先序递归遍历每个节点，再以每个节点作为起始点递归寻找满足条件的路径。

      还是动态规划做吧，对于每一节点，维护一个sum_lst，其中存放的是当前节点若为某条目标路径的终点其可能的取值集和，
      每对兄弟节点的取值集和是相同，说不清楚了，具体看代码吧

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        sum_lst = [sum]
        return self.pathSum_1(root, sum_lst)

    def pathSum_1(self, root, sum_lst):
        count = 0
        sum = sum_lst[-1]
        if not root:
            return count
        count += sum_lst.count(root.val)
        sum_lst = [x - root.val for x in sum_lst]
        sum_lst.append(sum)
        count += self.pathSum_1(root.left, sum_lst)
        count += self.pathSum_1(root.right, sum_lst)
        return count

#___________________________________    练习1   ______________________________#
'''
    这题 还是比较有意思的，寻找 和为sum的路径数量，其实直观的思路还是进行递归法吧，DFS过程中，进行sum-path 值的判别，获取满足的
    路径。

'''


#  比较容易理解的是使用  双重递归解法，按sum差值  去 DFS 遍历判别即可。   但是要顾虑好从每个位置可以作为开始和结尾，所以要双重形式
#  时间复杂度为O(n^2)   空间复杂度最优为O(n^2)
class Solution1(object):
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


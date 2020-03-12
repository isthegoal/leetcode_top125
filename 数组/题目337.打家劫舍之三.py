# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
      这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，
      聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
      如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

        示例 1:
        Input: [3,2,3,null,3,null,1]

             3
            / \
           2   3
            \   \
             3   1


        输出: 7
        解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

      分析：


      思路：每次只需要检查下已层抢和不抢的最大结果即可。即当前知道下一层的最大值和下两层的最大值。
      那么当前层的最大值便可以得到。

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root) :
            if not root : return [0, 0]
            robLeft = dfs(root.left)
            robRight = dfs(root.right)
            norobCur = robLeft[1] + robRight[1]
            robCur = max(robLeft[0] + robRight[0] + root.val, norobCur)
            return [norobCur, robCur]
        return dfs(root)[1]



# 另一种思路  （感觉这个更简洁些）
#只需后续遍历：其中返回值是抢root的最大金额，不抢root的最大金额。
#递归访问后返回二者的最大值
class Solution1(object):
    def rob(self, root):
        def postorder(root):
            if root == None:
                return (0,0)
            l = postorder(root.left)
            r = postorder(root.right)
            #  后半部分就是说如果不抢这个房屋，那么，它的左右子节点抢和不抢都可以，所以要max（抢， 不抢），看哪个大
            return  (root.val+l[1]+r[1],  max( l[0], l[1]) + max(r[0],r[1]) )
        r = postorder(root)
        return max(r[0],r[1])




#___________________________________    练习1   ______________________________#
# 这题可以理解为  二叉树的  最大累积值遍历，   必须是有间隔的行走
#  获取盗窃金额最大值
# 这题就 使用 dfs 深度 递归方法求解吧
#   每个节点返回两个值，第一个值为偷这家和不偷这家的最大值，第二个值是不偷这家，偷下两家的值。（两者可以深切思考下）
#   其中返回值是抢root的最大金额，不抢root的最大金额。
#https://leetcode-cn.com/problems/house-robber-iii/solution/dfs-by-jie-fang-qu-de-tian-0416/  有动态视频
def fun1(root):
    def dfs(root):
        #  针对空树的处理
        if not root:
            return [0,0]

        # 这两个的含义，是理解的核心，prel是直接的左右  累加和，不是最大求解的，其用途是逐步上层
        robleft,prel=dfs(root.left)
        robright,prer=dfs(root.right)

        # 比较重要的部分。   切记这里max使用的原因  就在于动态规划的核心思想： 最优局部子结构（之前统计的max就设定是之前最优的）
        # prel+prer+root.val是偷这家的最大值，robleft+robright是不偷这家的最优值。   prel+prer含义是不管这家，左右家的值。
        return max(prel+prer+root.val,robleft+robright),prel+prer

    #  最后返回从头结点返回的最大值
    return dfs(root)[0]

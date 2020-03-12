# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
           机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
           问总共有多少条不同的路径？


          例1：  输入: m = 3, n = 2
                输出: 3
                解释:
                从左上角开始，总共有 3 条路径可以到达右下角。
                1. 向右 -> 向右 -> 向下
                2. 向右 -> 向下 -> 向右
                3. 向下 -> 向右 -> 向右

      分析：简单动态规划法就可以


      思路：动态规划。
            dp[i][j] = dp[i-1][j] + dp[i][j-1]。注意边界条件。第一行或者第一列都只有一种走法。

'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * m] * n
        # print dp
        for i in range(n):
            for j in range(m):
                # print i, j
                if not i and not j:
                    dp[i][j] = 1
                elif not i and j:
                    dp[i][j] = 1
                elif i and not j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                # print dp
        return dp[-1][-1]


#___________________________________    练习1   ______________________________#
'''
     针对m x n 网格,这里就用动态规划思想吧，一个方程就可以解决。
    
     创建dp状态表示,dp[i][j]表示从左上角 走到i,j位置点有多少条不同的路径。
     （且每次只能往右走一步，或者往下走一步）
'''
def fun1(m,n):
    # 创建 状态吧，状态就是上面所表示的含义
    dp=[[0 for _ in range(n)] for _ in range(m)]

    # 对状态进行初始化， 如果是在左边一列和 上边一行，那么 直接都是对应一条路径即可
    for i in range(m):
        dp[i][0]=1
    for j in range(n):
        dp[0][j]=1

    # 进行核心的状态转移变化过程
    for i in range(m):
        for j in range(n):
            # 一行状态转移即可   (每个位置的状态是  由 上面一个 和 左边一个的路径加 一起得到的， 这是由走路形式限定的)
            dp[i][j]=dp[i-1][j]+dp[i][j-1]

    # 跟编辑距离一样，最后就是剩下的目标。
    return dp[-1][-1]

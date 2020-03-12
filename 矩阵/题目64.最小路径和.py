# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
      说明：每次只能向下或者向右移动一步。

          示例:
            输入:
            [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]
            输出: 7
            解释: 因为路径 1→3→1→1→1 的总和最小。

      分析：

      思路：  使用动态规划法即可
              dp[m][n] = min(dp[m - 1][n], dp[m][n - 1]) + grid[m][n]。注意考虑边界条件。
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #dp[m][n] = min(dp[m - 1][n], dp[m][n - 1]) + grid[m][n]
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * (n)] * (m)
        for i in range(m):
            for j in range(n):
                # print dp, i, j
                if not i and not j:
                    dp[i][j] = grid[i][j]
                elif i and not j:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif not i and j:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
#___________________________________    练习1   ______________________________#
'''
    找最短路径的问题，从左上点  到  右下点。
    
    思路 可以使用动态规划的思想，来进行判别路径长度，并进行累计，找到 最短长度的路径。（是最为常用和典型的 一道动态规划题。）
     
     【1】状态定义：设 dp 为大小 m×n 矩阵，其中 dp[i][j]的值代表直到走到 (i,j)的最小路径和。
     
     【2】状态初始化：dp 初始化即可，不需要修改初始 0 值。
     
     【3】状态转移方程 基本形式为：
     
         走到当前单元格 (i,j)的最小路径和=“从左方单元格(i−1,j)与从上方单元格(i,j−1) 走来的两个最小路径和中较小的”+当前单元格值grid[i][j]
     
     具体下来，可以分为四种情况：  [非常非常典型的动态规划思路。 很好理解]
         (1)当左边和上边都不是矩阵边界时： 即当i != 0,j!=0时，dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]；
                有两种可能性，按照两种情况走过来即可。从上面或者左边走过来。自然走动过来。
         (2)当只有左边是矩阵边界时： 只能从上面来，即当i=0,j!=0时， dp[i][j]=dp[i][j−1]+grid[i][j] ；  （走在最上边一行时，算从左边过来的）
         (3)当只有上边是矩阵边界时： 只能从左面来，即当i!=0,j=0时， dp[i][j]=dp[i−1][j]+grid[i][j] ；  （走在最左边一列时，算从上面过来的）
         (4)当左边和上边都是矩阵边界时： 即当i=0,j=0时，其实就是起点， dp[i][j]=grid[i][j]；         


    上面算法的   时间复杂度  O(M×N) ： 遍历整个 gridgrid 矩阵元素。
                 空间复杂度 O(1) ： 直接修改原矩阵，不使用额外空间

'''
def minpath(grid):
    #   这里直接在本身进行调整，所以 本身的grid形式就是 状态的载体。   grid有长宽 非正方形的（i是行，j是列）
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #  对于  网格中的每个位置，进行如下的 状态转移上的操作

            #  (4)如果是起点位置
            if i==j==0:
                continue

            #  (2)这个是左边  是矩阵边界的情况（走在最左边一列时）
            elif i==0:
                grid[i][j]=grid[i][j-1]+grid[i][j]

            # (3)这个是 上边 为矩阵边界的情况（走在最上面一行时）
            elif j==0:
                grid[i][j]=grid[i-1][j]+grid[i][j]

            # (1)这个是动态规划中核心 转移部分， 走在中间位置的 状态转移计算情况。
            else:
                grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]

    # 最终返回  目标状态位置即可
    return grid[-1][-1]




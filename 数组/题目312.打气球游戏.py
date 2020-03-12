# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定n个气球，索引从0到n-1。每个气球上画有一个数字，由数组nums表示。 你想让所有气球爆裂。
      如果您爆破气球i，您将得到nums [left] * nums [i] * nums [right]个硬币。 这里的左和右是i的相邻索引。
      爆发后，左右会相邻。明智地吹气球，找到可以收集的最大硬币数。

       Example:
        Given [3, 1, 5, 8]
        Return 167
        nums = [3,1,5,8] --> [3,5,8] -->  [3,8]  -->  [8]  -->  []
        coins = 3*1*5     +    3*5*8   +   1*3*8  + 1*8*1 =  167


      分析：

      思路： 使用动态规划解法即可

      动态规划的两个基本条件：
        （1）最优子结构：每个区间都符合这样解的结构。
        （2）重叠子问题：例如上题中，左右区间又生成左右区间，构成重叠问题。

'''
# @Time   :2018/6/22
# 解题思路 区间动态规划

class Solution:
    def maxCoins(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]  # 清除为0的数字，因为0不会得分，然后首尾添加[1],方便计算
        n = len(nums)
        dp = [[0] * n for _ in range(n)]  # 初始化dp
        for k in range(2, n):  # k 确定一个滑动窗口的大小，从2开始
            for left in range(0, n - k):  # 滑动窗口，从左向右滑动，确定区间的开始（left）、结束（right）位置
                right = left + k
                for i in range(left + 1, right):  # 开始枚举，区间内哪一个数字作为最后一个被戳破，使其得分最高
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]

if __name__ == '__main__':
    nums = [3,1,5,8]
    solu = Solution()
    out = solu.maxCoins(nums)
    print(out)
#___________________________________    练习1   ______________________________#
# 这里 每次选择戳破一个球， 然后计算球代表数字所带来的硬币值，  通过这样的计算来收集硬币，   找到方法计算能够获得的最大硬币值。
# 这里从题型上  可以看出，应该使用动态规划的解法。
'''
    1.预处理 nums = [1] + nums + [1], 给原数组首尾添加1, 并设新的数组大小为n
    2.状态dp[i][j] 表示删除nums[i+1,..., j-1]之后的最大值，我们的目标是求dp[0][n-1]
    3.状态转移方程 dp[i][j] = max{dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]}, i+1 <= k <= j-1
    4.填充dp的方式，反斜三角
    5.初始化 d[i][i+2] = nums[i] * nums[i+1] * nums[i+2]
    
    
    另一个解释：（同一问题下，较为有趣的解法）
        利用数组dp[i][j]记录i-j区间最多的硬币数；
        为了获取i-j之间的最大硬币数，我们要将i-j区间划分成长度为1,2,....,j-i+1长度的区间，分别去求每个小区间的最大硬币数；
        每个区间用k去遍历就是求[i,k-1],[k],[k+1,j]的最大硬币数，假设[i,k-1]、[k+1,j]已经求得，那当前k的硬币数就是nums[k]nums[i-1]nums[j+1]，[i,j]的最大硬币数就是 [i,k-1],[k],[k+1,j]三个区间硬币数之和。
            那么，dp[i][j]=max(dp[i][j],nums[k]nums[i-1]nums[j+1]+dp[i][k-1]+dp[k+1][j]);
'''
def fun1(iNums):
    #  首先 进行一些边界上的调整和设置，对数组进行重定
    nums=[1]+[i for i in iNums if i>0]+[1]

    #初始化dp状态          dp[i][j] 表示删除nums[i+1,..直到., j-1]之后的最大值
    n=len(nums)
    dp=[[0]*n for _ in range(n)]

    #进行 第三步  状态转移       三个for循环的把握十分重要，设定了从左到右判别的过程，对left、i、right不断的做调整
    for k in range(2,n):
        for left in range(0,n-k):# 滑动窗口，从左向右滑动，确定区间的开始（left）、结束（right）位置
            right=left+k
            for i in range(left+1,right):
                #最为核心的 状态转移方程, 对新的最大金币值的更新计算。 （非常好理解的动态规划转移方程）
                dp[left][right]=max(dp[left][right],nums[left]*nums[i]*nums[right]+dp[left][i]+dp[i][right])
    # 最后要获取到的状态目标
    return dp[0][n-1]




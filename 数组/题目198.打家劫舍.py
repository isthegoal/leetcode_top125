# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋
      装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
      给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

        输入: [1,2,3,1]
        输出: 4
        解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
             偷窃到的最高金额 = 1 + 3 = 4 。
      分析：

      思路：

        考虑前i项的结果dp[i]时，
        当i = 1， 返回dp[0] = nums[0]
        当i = 2， 返回dp[1] = max(nums[0], nums[1])
        当i = 3， 分为偷3号房屋和不偷3号房屋，
                 偷的情况下， 2号就不能偷了，结果为nums[2] + dp[0]
                 不偷的情况下，结果为dp[1]
                 所以返回dp[2] = max(dp[0] + nums[2], dp[1])
        ...

        以此类推，dp[i] = max(dp[i-2] + nums[i], dp[i-1])
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return 0
        if not nums:
            return 0
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(dp[0], nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

#___________________________________    练习1   ______________________________#
# 这里  很明显的是动态规划方法，而且每个行为都是可以琢磨的，  其实就是 状态-执行动作-获取新状态的  类似强化学习的过程，在这一过程中统计最大奖励max
# 对应dp方程是：dp[i] = max(dp[i-2]+nums[i], dp[i-1])
def fun1(nums):
    #  边界条件设定
    if not nums:
        return 0

    #定义 状态并初始化， 表示当前位置下获取的 金额
    dp=[0 for _ in nums]
    dp[0]=nums[0]

    #下面进行状态的转移
    for i in range(1,len(nums)):
        # 第一家的处理情况，   因为后面的通用式子是i-2，所以这里需要单独处理
        if i==1:
            dp[i]=max(dp[0],nums[i])
        # 有间隔取值 并累加的判断。   下面进行了综合的考虑，前一个和前两个上
        else:
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
    #返回最终的最大值即可
    return dp[-1]

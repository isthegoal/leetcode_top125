# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个无序的整数数组，找到其中最长上升子序列的长度。

            示例:

            输入:
            [10,9,2,5,3,7,101,18]
            输出: 4
            解释: 最长的上升子序列是
            [2,3,7,101]，
            它的长度是
            4

      分析：


      思路：
          感觉传统思路就够了，使用DP解法。

          用dp[i] 表示 从下标0 到下标i 的最长上升子序列的长度，例如对于样例输入[10,9,2,5,3,7,101,18], 
          有 dp = [ 1, 1, 1, 2, 2, 3, 4, 4]。
          显然dp[0] = 1，对于任意的i 不为零的情况，应该在 i 的左侧找一个下标 j ，其满足两个条件：
            1. nums[ j ]比 nums[ i ] 小
            2. 它是所有满足条件1里 dp [j]  最大的那个
            dp[i] = max(dp[j]) + 1 , j < i and nums[ j ] < nums[ i ]
          如果不存在这样的下标j，说明在0 ~ i - 1 的范围内，所有元素都比nums[i] 大，即无法找到一个能和 nums[i]
          组成上升子序列的元素，所以dp[i] = 1， 表示为nums[i] 自身成为一个长度为1 的上升子序列。


'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if not l:
            return 0
        dp = [1 for _ in range(l)]

        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

#___________________________________    练习1   ______________________________#
#  极其典型的动态规划问题，    感觉就是收集问题，这里是要获得 最长上升子序列的长度值（注意这里是 没有要求必须是连续子序列，所以更加灵活些）

def fun1(nums):
    # 边界条件
    l = len(nums)
    if l <= 1:
        return l

    # 定义 状态     明白其含义 dp[i] 表示 从下标0 到下标i 的最长上升子序列的长度,也就是直接目标意义
    dp = [1 for _ in range(l)]

    # 设定状态转移
    for i in range(1, l):
        for j in range(i):
            # 因为之前没有 设定必须连续，所以可以这样模糊的动态探索即可，能够 有间隔的组成递增序列。
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    # 最后选择 最大的状态情况
    return max(dp)
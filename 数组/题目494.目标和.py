# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个非负整数的集合nums和目标S，现在你有两个符号“+”和“-”，对于每个整数，你从这两个符号中选择其中一个作为
      该整数的标号。找到赋予标号后和为S的标记方法数。

                输入: nums: [1, 1, 1, 1, 1], S: 3
                输出: 5
                解释:

                -1+1+1+1+1 = 3
                +1-1+1+1+1 = 3
                +1+1-1+1+1 = 3
                +1+1+1-1+1 = 3
                +1+1+1+1-1 = 3

                一共有5种方法让最终目标和为3。

      分析：  这里是要求出有多少种方法 可以有效的 对数组元素进行 加减组合。



      思路：
      先使用数学思路，可以知道赋予标号后，集合中包含负数这正数，则有 sum(Positive)-sum(Negtive) = S。
      因为sum(Positive)+sum(Negtive)=sum(nums)，则有2*sum(Positive)=sum(nums)+S，故sum(Positive)=(sum(nums)+S)/2
      ，由于(sum(nums)+S)/2是固定的整数，所以只需要找到和为它的组合数即可。
      经过上述解析，可以将问题转化为从nums中找到和为(sum(nums)+S)/2的组合个数。这个问题可以通过动归来解决，
      用dp[i]存储和为i的组合数，然后对nums中的整数n进行遍历，对于所有i>=n的i，则有dp[i]=dp[i]+dp[i-n]


'''
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if sum(nums)<S:
            return 0
        if (S+sum(nums))%2==1:
            return 0
        target = (S+sum(nums))/2
        print(target)
        dp = [0]*(target+1)
        dp[0] = 1
        for n in nums:
            i = target
            while(i>=n):
                dp[i] = dp[i] + dp[i-n]
                i = i-1
        return dp[target]

#___________________________________    练习1   ______________________________#
'''
   这题是相当精妙的，主要参考这里的题解。https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/
   有三种可行的方法
     【1】DFS深度优先遍历
     【2】01背包问题
     【3】纯动态规划解法
     
     
感觉常用的方法 就这些。
   
     这里选用 01背包问题的解决方式，首先 将原问题转换成 01背包问题，然后再针对转换好的背包 设计状态和状态转移方程式，从而使用动态规划法进行求解。
     
     原问题是给定一些数字，加加减减，使得它们等于targert。例如，1 - 2 + 3 - 4 + 5 = target(3)。如果我们把加的和减的结合在一起，可以写成

        (1+3+5)  +  (-2-4) = target(3)
        -------     ------
         -> 正数    -> 负数
    
     所以，我们可以将原问题转化为： 找到nums一个正子集和一个负子集，使得总和等于target，统计这种可能性的总数。我们假设P是正子集，N是负子集。
     让我们看看如何将其转换为子集求和问题：
     
     因此题目转化为01背包，也就是能组合成容量为sum(P)的方式有多少种,一种组合中每个数字只能取一次。解决01背包问题使用的是动态规划的思想。
       开辟一个长度为P+1的数组，命名为dp的第x项，代表组合成数字x有多少方法。比如说,dp[0] = 1，代表组合成0只有1中方法，即什么也不取。
       比如说dp[5] = 3 ，代表使总和加到5总共有三种方法。所以最后返回的就是dp[P]，代表组合成P的方法有多少种。
'''
def fun1(nums,S):
    # 边界设定
    if (nums == None) or (len(nums) == 0):
        return 0

    # 边界条件
    sums = sum(nums)
    if sums < S or (S + sums) % 2 == 1:
        return 0

    # 初始状态设定
    p = (S + sums) / 2
    dp = [0 for i in range(p + 1)]
    dp[0] = 1

    # 状态转移方程
    for num in nums:
        for i in range(p, num - 1, -1):
            dp[i] += dp[i - num]

    return dp[p]


